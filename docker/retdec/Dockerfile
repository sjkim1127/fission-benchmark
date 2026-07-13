# RetDec v5 prebuilt Linux release + FastAPI adapter (amd64).
FROM --platform=linux/amd64 debian:bookworm-slim

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        ca-certificates \
        curl \
        python3 \
        python3-pip \
        python3-venv \
        xz-utils \
    && rm -rf /var/lib/apt/lists/*

# Official Avast RetDec release (matches decompiler-explorer pin).
ENV RETDEC_ROOT=/opt/retdec
RUN mkdir -p /tmp/retdec-dl \
    && curl -fsSL -o /tmp/retdec-dl/retdec.tar.xz \
        "https://github.com/avast/retdec/releases/download/v5.0/RetDec-v5.0-Linux-Release.tar.xz" \
    && mkdir -p "$RETDEC_ROOT" \
    && tar -xJf /tmp/retdec-dl/retdec.tar.xz -C "$RETDEC_ROOT" --strip-components=0 \
    && rm -rf /tmp/retdec-dl \
    && (test -x "$RETDEC_ROOT/bin/retdec-decompiler" \
        || test -x "$RETDEC_ROOT/retdec/bin/retdec-decompiler" \
        || ls -laR "$RETDEC_ROOT" | head -80)

# Normalize binary path (tarball layout varies slightly by packaging).
RUN if [ -x /opt/retdec/bin/retdec-decompiler ]; then \
      ln -sf /opt/retdec/bin/retdec-decompiler /usr/local/bin/retdec-decompiler; \
    elif [ -x /opt/retdec/retdec/bin/retdec-decompiler ]; then \
      ln -sf /opt/retdec/retdec/bin/retdec-decompiler /usr/local/bin/retdec-decompiler; \
    else \
      BIN=$(find /opt/retdec -type f -name retdec-decompiler | head -1); \
      test -n "$BIN" && ln -sf "$BIN" /usr/local/bin/retdec-decompiler; \
    fi \
    && retdec-decompiler --version | head -5

WORKDIR /app
COPY requirements.txt .
RUN python3 -m venv /opt/venv \
    && /opt/venv/bin/pip install --no-cache-dir -r requirements.txt
ENV PATH="/opt/venv/bin:$PATH"

COPY boundary.py server.py ./

EXPOSE 8000
ENV RETDEC_BIN=/usr/local/bin/retdec-decompiler
CMD ["python3", "-m", "uvicorn", "server:app", "--host", "0.0.0.0", "--port", "8000"]
