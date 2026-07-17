FROM debian:bookworm-slim

ENV DEBIAN_FRONTEND=noninteractive

# C/C++ mingw toolchains for primary PE semantic cohort.
# Rust/Go toolchains land in a later stage (lang_rust / lang_go profiles).
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        binutils \
        binutils-mingw-w64-x86-64 \
        binutils-mingw-w64-i686 \
        ca-certificates \
        gcc \
        g++ \
        gcc-mingw-w64-x86-64 \
        g++-mingw-w64-x86-64 \
        gcc-mingw-w64-i686 \
        libc6-dev \
        python3 \
        python3-yaml \
        clang \
        llvm \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /workspace
