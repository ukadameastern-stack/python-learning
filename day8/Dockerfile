# ---------- Stage 1: Build ----------
FROM python:3.11-slim AS builder

WORKDIR /app

# System deps (for psycopg2 etc.)
RUN apt-get update && apt-get install -y build-essential libpq-dev

COPY requirements.txt .
RUN pip install --user -r requirements.txt

# ---------- Stage 2: Runtime ----------
FROM python:3.11-slim

WORKDIR /app

# Runtime deps only
RUN apt-get update && apt-get install -y libpq5 netcat-openbsd

# Copy installed packages from builder
COPY --from=builder /root/.local /root/.local
ENV PATH=/root/.local/bin:$PATH

# Copy project
COPY . .

# Make start script executable
RUN chmod +x start.sh

CMD ["./start.sh"]