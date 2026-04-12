import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Action(BaseModel):
    decision: str

@app.get("/")
def health():
    return {"status": "running"}

@app.post("/reset")
def reset():
    return {"observation": "Environment reset."}

@app.post("/step")
def step(action: Action):
    return {"observation": f"Action {action.decision} taken", "reward": 1.0, "done": False}

# Required for Phase 1 validator
def main():
    uvicorn.run(app, host="0.0.0.0", port=7860)

if __name__ == "__main__":
    main()
