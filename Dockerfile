FROM python:3.10-slim
WORKDIR /app
RUN apt-get update && apt-get install -y git && rm -rf /var/lib/apt/lists/*
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

# Force remove any existing 'server' to prevent the "File exists" error
RUN rm -rf server && mkdir -p server && ln -s /app/app.py /app/server/app.py

EXPOSE 7860
CMD ["python", "-m", "app"]
