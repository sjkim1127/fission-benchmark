FROM radare/radare2:latest

USER root
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential git pkg-config python3 python3-pip python3-venv curl unzip zlib1g-dev \
    && rm -rf /var/lib/apt/lists/*

# Install r2ghidra decompiler plugin
RUN r2pm -U && r2pm -ci r2ghidra

WORKDIR /app
RUN python3 -m venv /opt/venv
ENV PATH="/opt/venv/bin:${PATH}"
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY server.py .
COPY boundary.py .

EXPOSE 8000
CMD ["python3", "-m", "uvicorn", "server:app", "--host", "0.0.0.0", "--port", "8000"]
