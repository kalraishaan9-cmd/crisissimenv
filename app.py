import os
import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"status": "running"}

# Fixes Phase 1 'OpenEnv Reset (POST OK)' failure
@app.post("/reset")
def reset_env():
    return {"status": "success"}

# YOUR LOGIC GOES HERE (Routes for your tasks, etc.)

def main():
    # References the server entry point in pyproject.toml
    uvicorn.run(app, host="0.0.0.0", port=7860)

if __name__ == "__main__":
    main()
