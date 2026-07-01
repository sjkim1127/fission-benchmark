FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl python3 python3-pip python3-venv wget xz-utils \
    && rm -rf /var/lib/apt/lists/*

# Install RetDec from GitHub Releases
ARG RETDEC_VERSION=v5.0
RUN wget -q "https://github.com/avast/retdec/releases/download/${RETDEC_VERSION}/RetDec-v5.0-Linux-Release.tar.xz" \
    -O /tmp/retdec.tar.xz \
    && mkdir -p /opt/retdec \
    && tar -xf /tmp/retdec.tar.xz -C /opt/retdec --strip-components=1 \
    && rm /tmp/retdec.tar.xz

ENV PATH="/opt/retdec:${PATH}"

WORKDIR /app
COPY requirements.txt .
RUN python3 -m pip install --no-cache-dir -r requirements.txt

COPY server.py .

EXPOSE 8000
CMD ["python3", "-m", "uvicorn", "server:app", "--host", "0.0.0.0", "--port", "8000"]
