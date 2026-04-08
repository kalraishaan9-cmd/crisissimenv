from fastapi import FastAPI
from models import CrisisAction
from crisis_environment import CrisisEnvironment
import os

app = FastAPI()

# Task ID can be set via HF Environment Variables
task_id = os.getenv("TASK_ID", "phishing_scam")
env = CrisisEnvironment(task_id=task_id)

@app.get("/")
def read_root():
    return {"status": "CrisisSim API is Running", "task": task_id}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/reset")
def reset():
    return env.reset()

@app.post("/step")
def step(action: CrisisAction):
    obs, reward, done, info = env.step(action)
    return {"observation": obs, "reward": reward, "done": done, "info": info}

@app.get("/state")
def state():
    return env.state()
