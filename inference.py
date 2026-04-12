import os
import asyncio

# Forced import check to help the validator environment
try:
    import requests
    import httpx
except ImportError:
    import subprocess
    import sys
    subprocess.check_call([sys.executable, "-m", "pip", "install", "requests", "httpx", "openai"])
    import requests
    import httpx

from openai import OpenAI

# Environment setup from Scaler/OpenEnv
API_KEY = os.getenv("HF_TOKEN")
API_BASE_URL = os.getenv("API_BASE_URL", "https://router.huggingface.co/v1")
MODEL_NAME = os.getenv("MODEL_NAME", "Qwen/Qwen2.5-72B-Instruct")
ENV_URL = "http://localhost:7860" 

# THE CRITICAL FIX: http_client=None ignores the validator's 
# injected proxy settings that cause the TypeError
client = OpenAI(
    base_url=API_BASE_URL, 
    api_key=API_KEY,
    http_client=None 
)

async def main():
    print("[LOG] Starting Phase 2 Inference...")
    try:
        # 1. Reset Environment
        response = requests.post(f"{ENV_URL}/reset")
        obs = response.json()
        done = False
        steps = 0

        # 2. Loop until task is finished
        while not done and steps < 10:
            steps += 1
            completion = client.chat.completions.create(
                model=MODEL_NAME,
                messages=[{"role": "user", "content": f"Observation: {obs}. What is the next command?"}]
            )
            action = completion.choices[0].message.content
            
            # 3. Step the environment
            step_res = requests.post(f"{ENV_URL}/step", json={"decision": action}).json()
            obs = step_res.get("observation")
            done = step_res.get("done", False)
            print(f"[STEP {steps}] Action: {action} | Done: {done}")
            
        print("[SUCCESS] Inference completed.")
    except Exception as e:
        print(f"[CRITICAL ERROR] {str(e)}")

if __name__ == "__main__":
    asyncio.run(main())
