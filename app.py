import os
import uvicorn
from fastapi import FastAPI
import openenv 

app = FastAPI()

@app.get("/")
def read_root():
    return {"status": "running"}

# Add your specific API logic/routes below this line

def main():
    # This function is what the 'server' script will call
    uvicorn.run("app:app", host="0.0.0.0", port=7860)

if __name__ == "__main__":
    main()
