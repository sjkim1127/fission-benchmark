#!/bin/sh
# Fission benchmark adapter entrypoint.
# FISSION_SOURCE=release  → image-baked GitHub Release CLI (CI default)
# FISSION_SOURCE=local    → runtime install from /opt/fission-local mount
set -eu

SOURCE="${FISSION_SOURCE:-release}"
LOCAL_ROOT="${FISSION_LOCAL_ROOT:-/opt/fission-local}"
CLI_DST="/usr/local/bin/fission_cli"
UTILS_DST="/opt/fission-utils/utils"
VERSION_FILE="/opt/fission-release-version"

install_local_bundle() {
  cli_src=""
  if [ -x "${LOCAL_ROOT}/fission_cli" ]; then
    cli_src="${LOCAL_ROOT}/fission_cli"
  elif [ -x "${LOCAL_ROOT}/bin/fission_cli" ]; then
    cli_src="${LOCAL_ROOT}/bin/fission_cli"
  else
    echo "error: FISSION_SOURCE=local but no executable fission_cli under ${LOCAL_ROOT}" >&2
    echo "  expected: ${LOCAL_ROOT}/fission_cli  (linux ELF matching container arch)" >&2
    echo "  run: scripts/prepare_local_fission.sh" >&2
    exit 1
  fi

  # Refuse Mach-O / wrong-arch host binaries early with a clear message.
  if command -v file >/dev/null 2>&1; then
    ft="$(file -b "$cli_src" 2>/dev/null || true)"
    case "$ft" in
      *ELF*)
        ;;
      *)
        echo "error: local fission_cli is not a Linux ELF (got: ${ft:-unknown})" >&2
        echo "  container needs a linux build; see scripts/prepare_local_fission.sh" >&2
        exit 1
        ;;
    esac
  fi

  install -m 755 "$cli_src" "$CLI_DST"

  utils_src=""
  if [ -d "${LOCAL_ROOT}/utils" ]; then
    utils_src="${LOCAL_ROOT}/utils"
  elif [ -d "${LOCAL_ROOT}/opt/fission-utils/utils" ]; then
    utils_src="${LOCAL_ROOT}/opt/fission-utils/utils"
  fi
  if [ -n "$utils_src" ]; then
    mkdir -p /opt/fission-utils
    rm -rf "$UTILS_DST"
    # Copy rather than symlink so nested relative paths stay stable.
    cp -a "$utils_src" "$UTILS_DST"
    ln -sfn "$UTILS_DST/sleigh-specs" /sleigh-specs
  fi

  sha="${FISSION_GIT_SHA:-unknown}"
  echo "local-${sha}" >"$VERSION_FILE"
  echo "local" >/opt/fission-source
  if [ -n "${FISSION_GIT_SHA:-}" ]; then
    echo "$FISSION_GIT_SHA" >/opt/fission-git-sha
  fi

  echo "[entrypoint] FISSION_SOURCE=local cli=${cli_src} sha=${sha}"
  "$CLI_DST" --version || true
}

case "$SOURCE" in
  local)
    install_local_bundle
    ;;
  release|"")
    echo "release" >/opt/fission-source
    if [ ! -x "$CLI_DST" ]; then
      echo "error: release image missing fission_cli at $CLI_DST" >&2
      exit 1
    fi
    ;;
  *)
    echo "error: unknown FISSION_SOURCE=${SOURCE} (use release|local)" >&2
    exit 1
    ;;
esac

export FISSION_SLEIGH_SPEC_DIR="${FISSION_SLEIGH_SPEC_DIR:-/sleigh-specs}"
export FISSION_RESOURCE_ROOT="${FISSION_RESOURCE_ROOT:-/opt/fission-utils/utils}"
export FISSION_GHIDRA_DATA_DIR="${FISSION_GHIDRA_DATA_DIR:-/opt/fission-utils/utils/ghidra-data}"
export FISSION_RELEASE_VERSION="${FISSION_RELEASE_VERSION:-$(cat "$VERSION_FILE" 2>/dev/null || echo unknown)}"
export FISSION_SOURCE="$SOURCE"

exec /opt/fission-server-venv/bin/python -m uvicorn server:app --host 0.0.0.0 --port 8000
