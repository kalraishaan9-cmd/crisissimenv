import os
import asyncio
import requests
from openai import OpenAI, DefaultHttpxClient

# Constants
API_BASE_URL = os.getenv("API_BASE_URL", "https://router.huggingface.co/v1")
API_KEY = os.getenv("HF_TOKEN")
MODEL_NAME = os.getenv("MODEL_NAME", "Qwen/Qwen2.5-72B-Instruct")
ENV_URL = "http://localhost:7860"

# THE PHASE 2 KILLER: trust_env=False prevents the 'proxies' TypeError
client = OpenAI(
    base_url=API_BASE_URL,
    api_key=API_KEY,
    http_client=DefaultHttpxClient(trust_env=False)
)

async def run_mission():
    print("[PHASE 2] Starting Mission...")
    try:
        # Reset Env
        obs = requests.post(f"{ENV_URL}/reset").json()["observation"]
        done = False
        
        while not done:
            # Agent decides
            response = client.chat.completions.create(
                model=MODEL_NAME,
                messages=[{"role": "user", "content": f"Env Obs: {obs}. What is your next move? Reply with 'finish' to end."}]
            )
            action = response.choices[0].message.content
            
            # Env steps
            res = requests.post(f"{ENV_URL}/step", json={"decision": action}).json()
            obs = res["observation"]
            done = res["done"]
            print(f"Agent Action: {action[:30]}... | Done: {done}")

        print("[SUCCESS] Phase 2 Cleared.")
    except Exception as e:
        print(f"[FAIL] Phase 2 Error: {e}")

if __name__ == "__main__":
    asyncio.run(run_mission())
