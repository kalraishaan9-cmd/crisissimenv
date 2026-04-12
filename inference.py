import os
import asyncio
import json
import requests
from openai import OpenAI

# Environment configuration
API_KEY = os.getenv("HF_TOKEN")
API_BASE_URL = os.getenv("API_BASE_URL", "https://router.huggingface.co/v1")
MODEL_NAME = os.getenv("MODEL_NAME", "Qwen/Qwen2.5-72B-Instruct")
ENV_URL = "http://localhost:7860" 

# THE FIX: http_client=None ignores the 'proxies' argument crashing your build
client = OpenAI(
    base_url=API_BASE_URL, 
    api_key=API_KEY,
    http_client=None 
)

async def main():
    task = os.getenv("TASK_ID", "phishing_scam")
    print(f"[START] task={task} env=CrisisSim model={MODEL_NAME}")
    
    try:
        # Reset the environment
        res = requests.post(f"{ENV_URL}/reset").json()
        obs = res
        done = False
        step_count = 0
        rewards = []

        while not done and step_count < 8:
            step_count += 1
            
            completion = client.chat.completions.create(
                model=MODEL_NAME,
                messages=[{"role": "user", "content": f"Crisis: {obs.get('scenario', '')}. Actions: {obs.get('history', '')}. Next action?"}]
            )
            action_text = completion.choices[0].message.content
            
            # Step the environment
            step_res = requests.post(f"{ENV_URL}/step", json={"decision": action_text}).json()
            obs = step_res["observation"]
            reward = step_res["reward"]
            done = step_res["done"]
            rewards.append(reward)
            
            print(f"[STEP] step={step_count} action={action_text[:30]} reward={reward:.2f} done={str(done).lower()}")
        
        score = min(sum(rewards), 1.0)
        print(f"[END] success={str(score > 0.5).lower()} steps={step_count} score={score:.2f}")
        
    except Exception as e:
        print(f"[ERROR] Inference failed: {str(e)}")

if __name__ == "__main__":
    asyncio.run(main())
