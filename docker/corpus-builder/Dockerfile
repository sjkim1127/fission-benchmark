FROM debian:bookworm-slim

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        binutils \
        binutils-mingw-w64-x86-64 \
        binutils-mingw-w64-i686 \
        ca-certificates \
        gcc \
        gcc-mingw-w64-x86-64 \
        gcc-mingw-w64-i686 \
        libc6-dev \
        python3 \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /workspace
