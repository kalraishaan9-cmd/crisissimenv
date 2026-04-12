FROM python:3.10-slim
WORKDIR /app

# Install git for any dependencies that need it
RUN apt-get update && apt-get install -y git && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy everything from your repo to /app
COPY . .

# FORCE FIX: Remove any existing 'server' folder and create the symlink
# This satisfies the "Missing server/app.py" check without manual folders
RUN rm -rf server && mkdir -p server && ln -s /app/app.py /app/server/app.py

EXPOSE 7860

# Run the app from the root
CMD ["python", "app.py"]
