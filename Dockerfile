FROM python:3.10-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y git && rm -rf /var/lib/apt/lists/*

# Upgrade build tools
RUN pip install --no-cache-dir --upgrade pip setuptools wheel

# Install all dependencies from requirements.txt
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code (this includes your pyproject.toml for the validator)
COPY . .

# BYPASS: We skip 'pip install .' because the environment is blocking it.
# We've already installed the requirements above, so the app will run fine.

EXPOSE 7860

# We run uvicorn directly. 
# Make sure your main file is named app.py and the FastAPI instance is named app.
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "7860"]
