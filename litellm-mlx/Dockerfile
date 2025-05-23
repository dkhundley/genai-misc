# Use a Python image with uv pre-installed
FROM ghcr.io/astral-sh/uv:python3.12-bookworm-slim

# Install the project into `/app`
WORKDIR /app

# Copy the project files
COPY . /app

# Remove mlx from pyproject.toml
RUN sed -i '/mlx/d' pyproject.toml

# Sync dependencies without mlx
RUN uv sync --frozen

# Install mlx separately
RUN uv pip install mlx-lm

# Place executables in the environment at the front of the path
ENV PATH="/app/.venv/bin:$PATH"

# Reset the entrypoint, don't invoke `uv`
ENTRYPOINT []