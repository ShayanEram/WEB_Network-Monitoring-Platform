# Use official lightweight Python image
FROM python:3.11-slim

# Install system dependencies, curl, and xz-utils (needed for extracting Zig)
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    xz-utils \
    && rm -rf /var/lib/apt/lists/*

# Install uv package manager
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Install Zig (matching version 0.13.0 used in your local setup and CI)
ENV ZIG_VERSION=0.13.0
RUN ARCH=$(dpkg --print-architecture) && \
    if [ "$ARCH" = "amd64" ]; then ZIG_ARCH="x86_64"; \
    elif [ "$ARCH" = "arm64" ]; then ZIG_ARCH="aarch64"; \
    else echo "Unsupported architecture: $ARCH" && exit 1; fi && \
    curl -fsSL https://ziglang.org/download/${ZIG_VERSION}/zig-linux-${ZIG_ARCH}-${ZIG_VERSION}.tar.xz -o zig.tar.xz && \
    tar -xf zig.tar.xz -C /opt/ && \
    mv /opt/zig-linux-${ZIG_ARCH}-${ZIG_VERSION} /opt/zig && \
    ln -s /opt/zig/zig /usr/local/bin/zig && \
    rm zig.tar.xz

# Set working directory
WORKDIR /app

# Copy dependency files first to leverage Docker layer caching
COPY pyproject.toml uv.lock ./

# Install Python dependencies using uv
RUN uv sync --frozen --no-dev

# Copy the rest of the application code
COPY . .

# Expose the Flask port
EXPOSE 5000

# Run the application (engine_runner.py will invoke 'zig cc' on startup)
CMD ["uv", "run", "python", "app.py"]