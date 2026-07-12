FROM revng/revng:latest

USER root
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl python3 python3-pip \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY requirements.txt .
RUN python3 -m pip install --no-cache-dir -r requirements.txt

COPY server.py .
COPY disasm_helper.py .
COPY boundary.py .

EXPOSE 8000
CMD ["python3", "-m", "uvicorn", "server:app", "--host", "0.0.0.0", "--port", "8000"]
