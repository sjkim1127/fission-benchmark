FROM eclipse-temurin:21-jre-bookworm

RUN apt-get update && apt-get install -y --no-install-recommends \
    curl wget unzip python3 python3-pip python3-venv \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /opt

# Download Ghidra 12.x
ARG GHIDRA_VERSION=12.0
ARG GHIDRA_SHA=PLACEHOLDER
RUN wget -q "https://github.com/NationalSecurityAgency/ghidra/releases/download/Ghidra_${GHIDRA_VERSION}_build/ghidra_${GHIDRA_VERSION}_PUBLIC.zip" \
    -O ghidra.zip \
    && unzip -q ghidra.zip \
    && rm ghidra.zip \
    && mv ghidra_${GHIDRA_VERSION}_PUBLIC ghidra

WORKDIR /app

COPY requirements.txt .
RUN python3 -m pip install --no-cache-dir -r requirements.txt

COPY server.py .
COPY DecompileFunction.java /opt/ghidra_scripts/

EXPOSE 8000
CMD ["python3", "-m", "uvicorn", "server:app", "--host", "0.0.0.0", "--port", "8000"]
