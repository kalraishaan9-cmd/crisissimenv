import os
import asyncio
import requests
from openai import OpenAI

# Environment configuration
API_KEY = os.getenv("HF_TOKEN")
API_BASE_URL = os.getenv("API_BASE_URL", "https://router.huggingface.co/v1")
MODEL_NAME = os.getenv("MODEL_NAME", "Qwen/Qwen2.5-72B-Instruct")
ENV_URL = "http://localhost:7860" 

# THE CRITICAL FIX: http_client=None ignores system-injected proxies
# that cause the 'unexpected keyword argument proxies' crash
client = OpenAI(
    base_url=API_BASE_URL, 
    api_key=API_KEY,
    http_client=None 
)

async def main():
    print(f"[START] Task execution starting...")
    try:
        # Reset the environment
        res = requests.post(f"{ENV_URL}/reset").json()
        obs = res
        done = False
        step_count = 0

        while not done and step_count < 8:
            step_count += 1
            completion = client.chat.completions.create(
                model=MODEL_NAME,
                messages=[{"role": "user", "content": f"Context: {obs}. What is the next action?"}]
            )
            action = completion.choices[0].message.content
            
            # Step the environment
            step_res = requests.post(f"{ENV_URL}/step", json={"decision": action}).json()
            obs = step_res["observation"]
            done = step_res["done"]
            print(f"[STEP {step_count}] Action taken. Done: {done}")
        
        print("[END] Inference complete.")
    except Exception as e:
        print(f"[ERROR] {str(e)}")

if __name__ == "__main__":
    asyncio.run(main())
