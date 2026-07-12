FROM debian:bookworm-slim

ENV DEBIAN_FRONTEND=noninteractive

RUN dpkg --add-architecture i386 \
    && apt-get update \
    && apt-get install -y --no-install-recommends \
        ca-certificates \
        curl \
        gcc-mingw-w64-i686 \
        gcc-mingw-w64-x86-64 \
        python3 \
        python3-pip \
        python3-venv \
        wine \
        wine32:i386 \
        wine64 \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
RUN python3 -m venv /opt/venv
ENV PATH="/opt/venv/bin:${PATH}" \
    PYTHONPATH=/app \
    WINEDEBUG=-all

COPY docker/oracle/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY runner /app/runner
COPY docker/oracle/server.py /app/server.py
COPY docker/oracle/pe_loader_snippet.c /app/pe_loader_snippet.c

EXPOSE 8000
CMD ["python3", "-m", "uvicorn", "server:app", "--host", "0.0.0.0", "--port", "8000", "--workers", "1"]
