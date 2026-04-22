# Stage 1 - builder
FROM python:3.11-slim AS builder

WORKDIR /app

COPY requirements.txt .

RUN pip install --user --no-cache-dir -r requirements.txt


# Stage 2 - runtime
FROM python:3.11-slim

WORKDIR /app

# create non-root user FIRST
RUN useradd -m workeruser

# copy only installed dependencies
COPY --from=builder /root/.local /home/workeruser/.local

COPY . .

ENV PATH=/home/workeruser/.local/bin:$PATH

RUN chown -R workeruser:workeruser /app

USER workeruser

HEALTHCHECK --interval=10s --timeout=5s --retries=3 \
  CMD pgrep -f worker.py || exit 1

CMD ["python", "worker.py"]
