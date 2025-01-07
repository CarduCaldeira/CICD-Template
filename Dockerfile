FROM ubuntu:22.04 AS base

ENV NVIDIA_DRIVER_CAPABILITIES=compute,utility

RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
        gcc && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

FROM base AS development

ENV UV_COMPILE_BYTECODE=1 UV_LINK_MODE=copy

RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
        ca-certificates \
        curl \
        build-essential && \
    rm -rf /var/lib/apt/lists/*

ADD https://astral.sh/uv/install.sh /uv-installer.sh

RUN sh /uv-installer.sh && rm /uv-installer.sh

ENV PATH="/root/.local/bin/:$PATH"

RUN uv python install 3.12

WORKDIR /app

COPY uv.lock pyproject.toml .

RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --frozen --no-install-project --no-dev

FROM base AS runtime

COPY --from=development /root/.local/share/uv/python/ /root/.local/share/uv/python/
COPY --from=development /app/.venv/ /app/.venv/

WORKDIR /app
COPY /src/ ./src/

#docker build -t pytorch- .