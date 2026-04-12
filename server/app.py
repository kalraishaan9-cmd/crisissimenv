import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Action(BaseModel):
    decision: str

@app.post("/reset")
def reset():
    return {"observation": "Environment reset. Waiting for agent action."}

@app.post("/step")
def step(action: Action):
    # Logic for Phase 3: Simple response to agent
    return {
        "observation": f"Action received: {action.decision}",
        "reward": 1.0,
        "done": False
    }

# CRITICAL: This main function is required for the Phase 1 validator
def main():
    uvicorn.run(app, host="0.0.0.0", port=7860)

if __name__ == "__main__":
    main()
