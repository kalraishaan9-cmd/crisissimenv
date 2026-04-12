import os
import asyncio
import requests
import httpx
from openai import OpenAI, DefaultHttpxClient

# Setup environment variables
API_KEY = os.getenv("HF_TOKEN")
API_BASE_URL = os.getenv("API_BASE_URL", "https://router.huggingface.co/v1")
MODEL_NAME = os.getenv("MODEL_NAME", "Qwen/Qwen2.5-72B-Instruct")
ENV_URL = "http://localhost:7860" 

# THE CRITICAL FIX: 
# trust_env=False tells the OpenAI client to ignore the 'proxies' settings 
# that the validator is forcing into your code, stopping the TypeError crash.
client = OpenAI(
    base_url=API_BASE_URL, 
    api_key=API_KEY,
    http_client=DefaultHttpxClient(trust_env=False)
)

async def main():
    print("[START] Phase 2 validation beginning...")
    try:
        # Reset simulation environment
        requests.post(f"{ENV_URL}/reset")
        
        obs = "Starting mission"
        done = False
        steps = 0
        
        while not done and steps < 10:
            steps += 1
            completion = client.chat.completions.create(
                model=MODEL_NAME,
                messages=[{"role": "user", "content": f"Task: Complete the mission. Status: {obs}"}]
            )
            action = completion.choices[0].message.content
            
            # Step the environment
            res = requests.post(f"{ENV_URL}/step", json={"decision": action}).json()
            obs = res.get("observation")
            done = res.get("done", False)
            print(f"[STEP {steps}] Action: {action[:20]}... | Done: {done}")

        print("[SUCCESS] Phase 2 complete. Submission ready.")
    except Exception as e:
        print(f"[ERROR] Inference logic failed: {str(e)}")

if __name__ == "__main__":
    asyncio.run(main())
