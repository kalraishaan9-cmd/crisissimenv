FROM python:3.10-slim
WORKDIR /app

# Install git for any internal dependencies
RUN apt-get update && apt-get install -y git && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# CRITICAL: Fixes Phase 1 "Missing app.py" check
RUN rm -rf server && mkdir -p server && ln -s /app/app.py /app/server/app.py

EXPOSE 7860
# Run the environment server
CMD ["python", "app.py"]
