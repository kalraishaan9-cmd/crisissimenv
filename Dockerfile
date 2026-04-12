FROM python:3.10-slim

WORKDIR /app

# Install git for the HF environment
RUN apt-get update && apt-get install -y git && rm -rf /var/lib/apt/lists/*

# Install dependencies first for better caching
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy all files from your repo
COPY . .

# CRITICAL: Fix the "Missing server/app.py" error for the validator
# This removes any existing server folder and creates a symbolic link
RUN rm -rf server && mkdir -p server && ln -s /app/app.py /app/server/app.py

EXPOSE 7860

# Port 7860 is required for
