import os
import asyncio
import requests
import httpx
from openai import OpenAI, DefaultHttpxClient

# 1. Setup Environment from the Scaler dashboard
API_KEY = os.getenv("HF_TOKEN")
API_BASE_URL = os.getenv("API_BASE_URL", "https://router.huggingface.co/v1")
MODEL_NAME = os.getenv("MODEL_NAME", "Qwen/Qwen2.5-72B-Instruct")
ENV_URL = "http://localhost:7860" 

# 2. THE CRITICAL FIX: 
# trust_env=False forces the client to ignore the 'proxies' settings 
# that are currently crashing your Phase 2 run.
client = OpenAI(
    base_url=API_BASE_URL, 
    api_key=API_KEY,
    http_client=DefaultHttpxClient(trust_env=False)
)

async def main():
    print("[LOG] Aura Maxing: Starting Phase 2...")
    try:
        # Reset the hackathon simulation environment
        requests.post(f"{ENV_URL}/reset")
        
        obs = "Initial state"
        done = False
        
        while not done:
            # Get the next move from the LLM
            completion = client.chat.completions.create(
                model=MODEL_NAME,
                messages=[{"role": "user", "content": f"Task: Complete the mission. Current: {obs}"}]
            )
            action = completion.choices[0].message.content
            
            # Send the action to the environment
            res = requests.post(f"{ENV_URL}/step", json={"decision": action}).json()
            obs = res.get("observation")
            done = res.get("done", False)
            
            if done: break

        print("[SUCCESS] Mission complete.")
    except Exception as e:
        print(f"[FAIL] Error encountered: {str(e)}")

if __name__ == "__main__":
    asyncio.run(main())
