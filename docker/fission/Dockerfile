FROM debian:bookworm-slim

RUN apt-get update && apt-get install -y --no-install-recommends \
    curl ca-certificates python3 python3-pip python3-venv \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Download latest fission-cli from GitHub Releases
ARG FISSION_VERSION=latest
RUN set -eux; \
    if [ "$FISSION_VERSION" = "latest" ]; then \
        URL=$(curl -sf https://api.github.com/repos/sjkim1127/Fission/releases/latest \
              | grep '"browser_download_url"' \
              | grep 'fission_cli-x86_64-unknown-linux' \
              | head -1 \
              | sed 's/.*"\(https[^"]*\)".*/\1/'); \
    else \
        URL="https://github.com/sjkim1127/Fission/releases/download/${FISSION_VERSION}/fission_cli-x86_64-unknown-linux-musl"; \
    fi; \
    echo "Downloading fission-cli from: $URL"; \
    curl -L "$URL" -o /usr/local/bin/fission_cli; \
    chmod +x /usr/local/bin/fission_cli

# Python FastAPI server
COPY requirements.txt .
RUN python3 -m pip install --no-cache-dir -r requirements.txt

COPY server.py .

EXPOSE 8000
CMD ["python3", "-m", "uvicorn", "server:app", "--host", "0.0.0.0", "--port", "8000"]
