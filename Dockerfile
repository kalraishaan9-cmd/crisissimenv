FROM python:3.10-slim
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy all files
COPY . .

# CRITICAL: Fixes the Phase 1 "server/app.py missing" error
RUN mkdir -p server && ln -s /app/app.py /app/server/app.py

EXPOSE 7860
# Use the -m flag to run the app properly
CMD ["python", "app.py"]
