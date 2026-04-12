import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from crisis_environment import CrisisEnvironment

app = FastAPI()
env = CrisisEnvironment()

class ActionRequest(BaseModel):
    action: dict

@app.get("/")
def health():
    return {"status": "ok"}

@app.post("/reset")
def reset_env():
    return {"state": env.reset()}

@app.post("/step")
def step_env(request: ActionRequest):
    state, reward, done, info = env.step(request.action)
    return {
        "state": state,
        "reward": reward,
        "done": done,
        "info": info
    }

def main():
    # Port 7860 is required for Hugging Face Spaces
    uvicorn.run(app, host="0.0.0.0", port=7860)

if __name__ == "__main__":
    main()
