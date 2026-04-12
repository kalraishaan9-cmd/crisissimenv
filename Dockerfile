FROM python:3.10-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y git && rm -rf /var/lib/apt/lists/*

# Copy your files into the container
COPY . .

# Install the exact working version of openenv to avoid build crashes
RUN pip install --no-cache-dir fastapi uvicorn requests openai openenv==0.1.13

# Expose the internal port for the validator
EXPOSE 7860

# Run the app from the server folder
CMD ["python", "server/app.py"]
