FROM ubuntu:24.04

ENV DEBIAN_FRONTEND=noninteractive
ENV FISSION_SLEIGH_SPEC_DIR=/sleigh-specs
ENV FISSION_RESOURCE_ROOT=/opt/fission-utils/utils
ENV FISSION_GHIDRA_DATA_DIR=/opt/fission-utils/utils/ghidra-data

RUN apt-get update && apt-get install -y --no-install-recommends \
    curl ca-certificates python3 python3-pip python3-venv tar \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Download fission-cli and runtime specs from GitHub Releases.
ARG FISSION_VERSION=v0.2.0
ARG FISSION_ASSETS_TAG=assets-v1
RUN set -eux; \
    if [ "$FISSION_VERSION" = "latest" ]; then \
        URL=$(curl -sf https://api.github.com/repos/sjkim1127/Fission/releases/latest \
              | grep '"browser_download_url"' \
              | grep 'fission_cli-x86_64-unknown-linux' \
              | head -1 \
              | sed 's/.*"\(https[^"]*\)".*/\1/'); \
    else \
        URL="https://github.com/sjkim1127/Fission/releases/download/${FISSION_VERSION}/fission_cli-x86_64-unknown-linux-gnu"; \
    fi; \
    echo "Downloading fission-cli from: $URL"; \
    curl -L "$URL" -o /usr/local/bin/fission_cli; \
    chmod +x /usr/local/bin/fission_cli; \
    /usr/local/bin/fission_cli --version; \
    curl -L "https://github.com/sjkim1127/Fission/releases/download/${FISSION_ASSETS_TAG}/fission-utils.tar.gz" \
      -o /tmp/fission-utils.tar.gz; \
    mkdir -p /opt/fission-utils; \
    tar --warning=no-unknown-keyword -xzf /tmp/fission-utils.tar.gz -C /opt/fission-utils; \
    ln -s /opt/fission-utils/utils/sleigh-specs /sleigh-specs; \
    test -d /sleigh-specs/languages; \
    test -d /opt/fission-utils/utils/ghidra-data; \
    test -d /opt/fission-utils/utils/signatures; \
    rm /tmp/fission-utils.tar.gz

# Python FastAPI server
COPY requirements.txt .
RUN python3 -m venv /opt/fission-server-venv \
    && /opt/fission-server-venv/bin/pip install --no-cache-dir -r requirements.txt

COPY server.py .

EXPOSE 8000
CMD ["/opt/fission-server-venv/bin/python", "-m", "uvicorn", "server:app", "--host", "0.0.0.0", "--port", "8000"]
