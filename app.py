import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from crisis_environment import CrisisEnvironment

# 1. Initialize FastAPI and your Environment
app = FastAPI()
env = CrisisEnvironment()

# 2. Define the Action Schema
# This ensures the validator's JSON matches your environment's expectations
class ActionRequest(BaseModel):
    action: dict  # Or int/str depending on your specific environment logic

@app.get("/")
def health_check():
    return {"status": "running", "message": "CrisisSim API is active"}

@app.post("/reset")
def reset_env():
    """Resets the simulation to the starting state."""
    state = env.reset()
    return {"state": state}

@app.post("/step")
def step_env(request: ActionRequest):
    """Processes one turn in the simulation."""
    # Logic to pass the action into your crisis_environment.py
    state, reward, done, info = env.step(request.action)
    return {
        "state": state, 
        "reward": reward, 
        "done": done, 
        "info": info
    }

def main():
    """
    CRITICAL: The validator looks for this specific function 
    to start your server on port 7860.
    """
    uvicorn.run(app, host="0.0.0.0", port=7860)

if __name__ == "__main__":
    main()
