FROM ubuntu:24.04

ENV DEBIAN_FRONTEND=noninteractive
ENV FISSION_SLEIGH_SPEC_DIR=/sleigh-specs
ENV FISSION_RESOURCE_ROOT=/opt/fission-utils/utils
ENV FISSION_GHIDRA_DATA_DIR=/opt/fission-utils/utils/ghidra-data

RUN apt-get update && apt-get install -y --no-install-recommends \
    curl ca-certificates python3 python3-pip python3-venv tar \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Download fission-cli and runtime utils from GitHub Releases.
# v0.1.1+: assets are:
#   fission-linux-x64.tar.gz        (contains: fission_cli + utils/)
#   fission_cli-x86_64-unknown-linux-gnu  (raw benchmark binary, same release)
ARG FISSION_VERSION=latest
RUN set -eux; \
    if [ "$FISSION_VERSION" = "latest" ]; then \
        RELEASE_JSON=$(curl -sf https://api.github.com/repos/sjkim1127/Fission/releases/latest); \
        CLI_URL=$(echo "$RELEASE_JSON" \
              | grep '"browser_download_url"' \
              | grep 'fission-linux-x64\.tar\.gz' \
              | head -1 \
              | sed 's/.*"\(https[^"]*\)".*/\1/'); \
    else \
        CLI_URL="https://github.com/sjkim1127/Fission/releases/download/${FISSION_VERSION}/fission-linux-x64.tar.gz"; \
    fi; \
    echo "Downloading fission bundle from: $CLI_URL"; \
    curl -L "$CLI_URL" -o /tmp/fission-bundle.tar.gz; \
    mkdir -p /opt/fission-utils; \
    tar --warning=no-unknown-keyword -xzf /tmp/fission-bundle.tar.gz -C /opt/fission-utils; \
    # The tar contains: fission_cli + utils/
    find /opt/fission-utils -name 'fission_cli' -exec cp {} /usr/local/bin/fission_cli \; ; \
    chmod +x /usr/local/bin/fission_cli; \
    /usr/local/bin/fission_cli --version; \
    ln -sf /opt/fission-utils/utils/sleigh-specs /sleigh-specs; \
    test -d /sleigh-specs/languages; \
    test -d /opt/fission-utils/utils/ghidra-data; \
    test -d /opt/fission-utils/utils/signatures; \
    rm /tmp/fission-bundle.tar.gz

# Python FastAPI server
COPY requirements.txt .
RUN python3 -m venv /opt/fission-server-venv \
    && /opt/fission-server-venv/bin/pip install --no-cache-dir -r requirements.txt

COPY server.py .

EXPOSE 8000
CMD ["/opt/fission-server-venv/bin/python", "-m", "uvicorn", "server:app", "--host", "0.0.0.0", "--port", "8000"]
