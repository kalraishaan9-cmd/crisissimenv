from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

app = FastAPI()

class Action(BaseModel):
    decision: str

# Simple internal state for Phase 3 review
class State:
    def __init__(self):
        self.step_count = 0
        self.goal_reached = False

env_state = State()

@app.post("/reset")
def reset():
    global env_state
    env_state = State()
    return {"observation": "System initialized. Mission start."}

@app.post("/step")
def step(action: Action):
    env_state.step_count += 1
    # Simple logic: If the agent says "finish", end the mission
    if "finish" in action.decision.lower() or env_state.step_count >= 5:
        env_state.goal_reached = True
        
    return {
        "observation": f"Step {env_state.step_count} completed. Action taken: {action.decision}",
        "reward": 1.0 if env_state.goal_reached else 0.1,
        "done": env_state.goal_reached
    }

@app.get("/state")
def get_state():
    return {"steps": env_state.step_count, "goal": env_state.goal_reached}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=7860)
