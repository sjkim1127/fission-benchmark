#!/usr/bin/env bash
# Prepare a Linux fission_cli + utils bundle for docker-compose.local.yml.
#
# Mirrors Fission CD Linux matrix (see Fission/.github/workflows/cd.yml):
#   cargo build -p fission-cli --locked --release --target x86_64-unknown-linux-gnu
#
# Output (default): .local/fission-bundle/{fission_cli,utils/,GIT_SHA}
#
# Build preference order:
#   1. FISSION_LINUX_CLI=…          explicit prebuilt Linux ELF
#   2. existing target/…/fission_cli  reuse if already Linux ELF
#   3. host cargo zigbuild            macOS/dev machines with Zig (fast path)
#   4. host cargo --target            Linux x86_64 hosts (same as CD)
#   5. Docker rust:bookworm           last resort (cached volumes)
#
# Env:
#   FISSION_ROOT                 monorepo path (default: ../Fission)
#   FISSION_LOCAL_BUNDLE         output bundle dir
#   FISSION_LINUX_CLI            prebuilt Linux ELF (skip build)
#   FISSION_LINUX_TARGET         default x86_64-unknown-linux-gnu
#   FISSION_FORCE_DOCKER_BUILD=1 skip host builders; use Docker only
#   FISSION_DOCKER_PLATFORM      default linux/amd64 (matches compose)
#   FISSION_AUTO_INSTALL_ZIGBUILD=1  cargo install cargo-zigbuild when zig exists
#   FISSION_CARGO_LOCKED=0       drop --locked if local Cargo.lock is dirty
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
FISSION_ROOT="${FISSION_ROOT:-$(cd "$ROOT_DIR/../Fission" 2>/dev/null && pwd || true)}"
BUNDLE="${FISSION_LOCAL_BUNDLE:-$ROOT_DIR/.local/fission-bundle}"
FORCE_DOCKER="${FISSION_FORCE_DOCKER_BUILD:-0}"
LINUX_CLI_OVERRIDE="${FISSION_LINUX_CLI:-}"
LINUX_TARGET="${FISSION_LINUX_TARGET:-x86_64-unknown-linux-gnu}"
DOCKER_PLATFORM="${FISSION_DOCKER_PLATFORM:-linux/amd64}"
AUTO_ZIGBUILD="${FISSION_AUTO_INSTALL_ZIGBUILD:-1}"
LOCKED_FLAG="--locked"
if [[ "${FISSION_CARGO_LOCKED:-1}" == "0" ]]; then
  LOCKED_FLAG=""
fi

die() { echo "error: $*" >&2; exit 1; }
# Logs must go to stderr so command substitutions only capture paths.
info() { echo "[prepare-local] $*" >&2; }

if [[ -z "${FISSION_ROOT}" || ! -d "${FISSION_ROOT}" ]]; then
  die "FISSION_ROOT not found (set FISSION_ROOT=/path/to/Fission)"
fi
if [[ ! -d "${FISSION_ROOT}/utils" ]]; then
  die "missing ${FISSION_ROOT}/utils"
fi
if [[ ! -f "${FISSION_ROOT}/Cargo.toml" ]]; then
  die "FISSION_ROOT does not look like the Fission workspace: ${FISSION_ROOT}"
fi

mkdir -p "$BUNDLE"
GIT_SHA="$(git -C "$FISSION_ROOT" rev-parse --short HEAD 2>/dev/null || echo unknown)"
echo "$GIT_SHA" >"$BUNDLE/GIT_SHA"

TARGET_CLI="${FISSION_ROOT}/target/${LINUX_TARGET}/release/fission_cli"
NATIVE_CLI="${FISSION_ROOT}/target/release/fission_cli"

is_linux_elf_x64() {
  local p="$1"
  [[ -f "$p" && -x "$p" ]] || return 1
  if command -v file >/dev/null 2>&1; then
    local ft
    ft="$(file -b "$p" 2>/dev/null || true)"
    echo "$ft" | grep -qi 'ELF' || return 1
    # Prefer x86-64 for default compose platform linux/amd64.
    if [[ "$DOCKER_PLATFORM" == "linux/amd64" ]]; then
      echo "$ft" | grep -Eqi 'x86-64|x86_64|AMD64|Intel 80386' || {
        # Some `file` builds only say "ELF 64-bit LSB" — accept if also pie/exec.
        echo "$ft" | grep -qi '64-bit' || return 1
      }
    fi
  fi
  return 0
}

install_cli_to_bundle() {
  local src="$1"
  local dst="$BUNDLE/fission_cli"
  # Same-path (e.g. FISSION_LINUX_CLI already points at the bundle) is a no-op.
  if [[ "$(cd "$(dirname "$src")" && pwd)/$(basename "$src")" != \
        "$(cd "$(dirname "$dst")" 2>/dev/null && pwd)/$(basename "$dst")" ]]; then
    install -m 755 "$src" "$dst"
  else
    chmod 755 "$dst" 2>/dev/null || true
  fi
  is_linux_elf_x64 "$dst" \
    || die "installed CLI is not a usable Linux ELF: $src ($(file -b "$src" 2>/dev/null || echo unknown))"
}

have_cargo_zigbuild() {
  cargo zigbuild -h >/dev/null 2>&1
}

ensure_cargo_zigbuild() {
  have_cargo_zigbuild && return 0
  command -v zig >/dev/null 2>&1 || return 1
  [[ "$AUTO_ZIGBUILD" == "1" ]] || return 1
  info "installing cargo-zigbuild (one-time; Zig detected at $(command -v zig))"
  cargo install cargo-zigbuild --locked
  have_cargo_zigbuild
}

ensure_rust_target() {
  if command -v rustup >/dev/null 2>&1; then
    rustup target add "$LINUX_TARGET" >/dev/null 2>&1 || true
  fi
}

# CD-equivalent host build (Linux runner or zig-linked cross).
build_cli_host_cd_target() {
  local out="$TARGET_CLI"
  ensure_rust_target

  if ensure_cargo_zigbuild; then
    info "host cross-build (CD target): cargo zigbuild -p fission-cli ${LOCKED_FLAG} --release --target ${LINUX_TARGET}"
    (
      cd "$FISSION_ROOT"
      # shellcheck disable=SC2086
      cargo zigbuild -p fission-cli ${LOCKED_FLAG} --release --target "$LINUX_TARGET"
    )
    is_linux_elf_x64 "$out" || die "zigbuild produced non-Linux CLI at $out"
    echo "$out"
    return 0
  fi

  # Native Linux x86_64: same command as Fission/.github/workflows/cd.yml
  if [[ "$(uname -s)" == "Linux" && "$(uname -m)" =~ ^(x86_64|amd64)$ ]]; then
    info "host native build (CD): cargo build -p fission-cli ${LOCKED_FLAG} --release --target ${LINUX_TARGET}"
    (
      cd "$FISSION_ROOT"
      # shellcheck disable=SC2086
      cargo build -p fission-cli ${LOCKED_FLAG} --release --target "$LINUX_TARGET"
    )
    is_linux_elf_x64 "$out" || die "native build produced non-Linux CLI at $out"
    echo "$out"
    return 0
  fi

  return 1
}

build_cli_via_docker() {
  info "Docker build (CD-equivalent target ${LINUX_TARGET}, platform ${DOCKER_PLATFORM})..."
  info "  source: $FISSION_ROOT"
  info "  cargo registry/git/target caches: docker volumes fission-bench-*"

  # Persistent caches make rebuilds much cheaper than a cold rust:bookworm each time.
  docker volume create fission-bench-cargo-registry >/dev/null
  docker volume create fission-bench-cargo-git >/dev/null
  docker volume create fission-bench-cargo-target >/dev/null

  # The official Rust image exports Cargo through PATH. A login shell resets
  # that PATH on Debian and makes the fallback fail with `cargo: command not found`.
  docker run --rm \
    --platform "$DOCKER_PLATFORM" \
    -v "${FISSION_ROOT}:/src" \
    -v "${BUNDLE}:/out" \
    -v fission-bench-cargo-registry:/usr/local/cargo/registry \
    -v fission-bench-cargo-git:/usr/local/cargo/git \
    -v fission-bench-cargo-target:/src/target \
    -w /src \
    -e CARGO_TERM_COLOR=always \
    rust:bookworm \
    bash -c "
      set -euo pipefail
      apt-get update -qq
      DEBIAN_FRONTEND=noninteractive apt-get install -y -qq \
        pkg-config libssl-dev build-essential cmake git >/dev/null
      # Same package + flags as Fission CD (ubuntu-latest matrix row).
      cargo build -p fission-cli ${LOCKED_FLAG} --release --target ${LINUX_TARGET}
      install -m 755 target/${LINUX_TARGET}/release/fission_cli /out/fission_cli
      /out/fission_cli --version
    "
  is_linux_elf_x64 "$BUNDLE/fission_cli" || die "Docker build did not yield a Linux ELF CLI"
}

# ── Resolve CLI ──────────────────────────────────────────────────────────────

if [[ -n "$LINUX_CLI_OVERRIDE" ]]; then
  is_linux_elf_x64 "$LINUX_CLI_OVERRIDE" \
    || die "FISSION_LINUX_CLI is not a Linux ELF: $LINUX_CLI_OVERRIDE"
  info "using FISSION_LINUX_CLI=$LINUX_CLI_OVERRIDE"
  install_cli_to_bundle "$LINUX_CLI_OVERRIDE"
elif [[ "$FORCE_DOCKER" != "1" ]] && is_linux_elf_x64 "$TARGET_CLI"; then
  info "reusing CD-target artifact: $TARGET_CLI"
  install_cli_to_bundle "$TARGET_CLI"
elif [[ "$FORCE_DOCKER" != "1" ]] && is_linux_elf_x64 "$NATIVE_CLI"; then
  info "reusing native release artifact: $NATIVE_CLI"
  install_cli_to_bundle "$NATIVE_CLI"
elif [[ "$FORCE_DOCKER" != "1" ]] && BUILT="$(build_cli_host_cd_target)"; then
  info "host build ok: $BUILT"
  install_cli_to_bundle "$BUILT"
else
  if ! command -v docker >/dev/null 2>&1; then
    die "no Linux ELF CLI and no docker; install Docker or cargo-zigbuild+zig, or set FISSION_LINUX_CLI"
  fi
  build_cli_via_docker
fi

is_linux_elf_x64 "$BUNDLE/fission_cli" || die "bundle fission_cli is not a Linux ELF"

info "syncing utils from ${FISSION_ROOT}/utils"
rm -rf "$BUNDLE/utils"
cp -a "${FISSION_ROOT}/utils" "$BUNDLE/utils"

for need in sleigh-specs ghidra-data signatures; do
  [[ -d "$BUNDLE/utils/$need" ]] || die "utils missing $need"
done

ENV_SNIPPET="$ROOT_DIR/.env.local"
{
  echo "# Generated by scripts/prepare_local_fission.sh — do not commit"
  echo "FISSION_LOCAL_BUNDLE=$BUNDLE"
  echo "FISSION_GIT_SHA=$GIT_SHA"
  echo "FISSION_SOURCE=local"
  echo "FISSION_LINUX_TARGET=$LINUX_TARGET"
} >"$ENV_SNIPPET"

info "bundle ready: $BUNDLE"
info "  fission_cli: $(file -b "$BUNDLE/fission_cli" 2>/dev/null || echo ok)"
info "  git_sha:     $GIT_SHA"
info "  target:      $LINUX_TARGET (CD linux matrix)"
info "  env file:    $ENV_SNIPPET"
cat <<EOF

Next:
  set -a; source .env.local; set +a

  docker compose -f docker-compose.yml -f docker-compose.local.yml \\
    --profile local up -d --build fission

  curl -s "http://localhost:\${FISSION_HOST_PORT:-8007}/health" | jq .

  python runner/runner.py --corpus dev --decompilers fission \\
    --output "results/local_\${FISSION_GIT_SHA}.json" --no-publish

Build tips (macOS):
  # preferred one-liner after Zig is installed:
  brew install zig
  cargo install cargo-zigbuild --locked
  # then re-run this script (uses cargo zigbuild --target ${LINUX_TARGET})

  # or point at a prebuilt CD-compatible binary:
  FISSION_LINUX_CLI=/path/to/fission_cli ./scripts/prepare_local_fission.sh

IMPORTANT:
  - Local results are quality-loop observation only.
  - Do NOT promote them to results/latest.json / GitHub Pages.
  - CI always uses FISSION_SOURCE=release (GitHub Release bake).
EOF
