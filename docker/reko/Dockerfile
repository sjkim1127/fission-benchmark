FROM mcr.microsoft.com/dotnet/sdk:9.0 AS builder

# Install build dependencies
RUN apt-get update && apt-get install -y \
    cmake \
    libcapstone-dev \
    g++ \
    pkg-config \
    git \
    && rm -rf /var/lib/apt/lists/*

# Clone and build Reko
WORKDIR /tmp
RUN git clone --depth 1 https://github.com/uxmal/reko.git && \
    cd reko && \
    export DOTNET_ROLL_FORWARD=Major && \
    dotnet msbuild -p:Platform=x64 -p:Configuration=UnixRelease -t:build_solution -m ./src/BuildTargets/BuildTargets.csproj

# Use lightweight runtime image if possible, but dotnet decompile.dll requires dotnet runtime + capstone-dev
# We use dotnet sdk:9.0 image to make sure dotnet and compilers are correct, and keep it simple.
FROM mcr.microsoft.com/dotnet/sdk:9.0

# Install runtime dependencies
RUN apt-get update && apt-get install -y \
    libcapstone-dev \
    python3 \
    python3-pip \
    python3-venv \
    && rm -rf /var/lib/apt/lists/*

# Copy built Reko files from builder
COPY --from=builder /tmp/reko/src/Drivers/CmdLine/bin/x64/Release/net8.0 /opt/reko

# Copy server files
WORKDIR /app
COPY server.py /app/server.py

# Create virtual environment and install python dependencies
RUN python3 -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"
RUN pip install --no-cache-dir fastapi uvicorn pydantic

EXPOSE 8000
ENV REKO_BIN=/opt/reko/decompile.dll
CMD ["python3", "/app/server.py"]
