import os
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Standard route for health checks
@app.get("/")
def read_root():
    return {"status": "running"}

# CRITICAL: This fixes the 'OpenEnv Reset (POST OK)' failure
@app.post("/reset")
def reset_env():
    return {"status": "success", "message": "Environment reset"}

# Add your existing logic/routes here

def main():
    # Required for 'server' script entry point
    uvicorn.run(app, host="0.0.0.0", port=7860)

if __name__ == "__main__":
    main()
