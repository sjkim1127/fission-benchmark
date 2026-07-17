FROM debian:bookworm-slim

ENV DEBIAN_FRONTEND=noninteractive

# C/C++ mingw toolchains for primary PE semantic cohort.
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        binutils \
        binutils-mingw-w64-x86-64 \
        binutils-mingw-w64-i686 \
        ca-certificates \
        curl \
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

# Rust (minimal) + windows-gnu target for PE corpus builds.
ENV RUSTUP_HOME=/usr/local/rustup \
    CARGO_HOME=/usr/local/cargo \
    PATH=/usr/local/cargo/bin:/usr/local/go/bin:$PATH
RUN curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs \
    | sh -s -- -y --default-toolchain stable --profile minimal \
    && rustup target add x86_64-pc-windows-gnu \
    && rustc --version

# Go toolchain for CGO windows PE corpus builds.
ARG GO_VERSION=1.22.10
RUN curl -fsSL "https://go.dev/dl/go${GO_VERSION}.linux-amd64.tar.gz" -o /tmp/go.tgz \
    && tar -C /usr/local -xzf /tmp/go.tgz \
    && rm /tmp/go.tgz \
    && go version

WORKDIR /workspace
