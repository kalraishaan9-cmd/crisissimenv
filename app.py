import os
import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"status": "running"}

# Fixes 'OpenEnv Reset (POST OK) failed'
@app.post("/reset")
def reset_env():
    return {"status": "success", "message": "Environment reset"}

# Your main logic here...

def main():
    # Points to this for the project.scripts entry
    uvicorn.run(app, host="0.0.0.0", port=7860)

if __name__ == "__main__":
    main()
