FROM cincan/snowman-decompile:latest

USER root
RUN sed -i 's/deb.debian.org/archive.debian.org/g; s/security.debian.org/archive.debian.org/g' /etc/apt/sources.list \
    && sed -i '/buster-updates/d' /etc/apt/sources.list \
    && apt-get update \
    && apt-get install -y --no-install-recommends \
    curl python3 python3-pip \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY requirements.txt .
RUN python3 -m pip install --no-cache-dir -r requirements.txt

COPY server.py .
COPY disasm_helper.py .
COPY boundary.py .

ENTRYPOINT []
EXPOSE 8000
CMD ["python3", "-m", "uvicorn", "server:app", "--host", "0.0.0.0", "--port", "8000"]
