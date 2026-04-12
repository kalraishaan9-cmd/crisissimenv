from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
def home():
    return {"status": "running"}

@app.post("/reset")
def reset():
    return {"observation": {"scenario": "Initial crisis", "history": []}, "status": "success"}

@app.post("/step")
def step(data: dict):
    # Basic logic to keep the agent moving
    return {
        "observation": {"scenario": "Continuing crisis", "history": ["Action taken"]},
        "reward": 0.5,
        "done": False
    }

def main():
    uvicorn.run(app, host="0.0.0.0", port=7860)

if __name__ == "__main__":
    main()
