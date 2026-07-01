FROM ubuntu:22.04
ENV DEBIAN_FRONTEND=noninteractive

# Install dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    git \
    build-essential \
    cmake \
    qtbase5-dev \
    libcapstone-dev \
    flex \
    bison \
    python3 \
    python3-pip \
    python3-venv \
    curl \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# Clone and build Boomerang
RUN git clone --depth 1 https://github.com/BoomerangDecompiler/boomerang.git /opt/boomerang \
    && mkdir /opt/boomerang/build \
    && cd /opt/boomerang/build \
    && cmake -DCMAKE_BUILD_TYPE=Release -DLOG_TO_FILE=OFF .. \
    && make -j$(nproc) \
    && make install \
    && ldconfig

# Install FastAPI, Uvicorn, and disassembly helper libraries
RUN pip install --no-cache-dir fastapi uvicorn pydantic pefile pyelftools capstone

WORKDIR /app
COPY server.py .
COPY disasm_helper.py .

EXPOSE 8000
CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "8000"]
