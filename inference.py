import os
import requests
import time
from openai import OpenAI, DefaultHttpxClient

# trust_env=False is the required fix for the proxy crash in this environment
client = OpenAI(
    base_url="https://router.huggingface.co/v1",
    api_key=os.getenv("HF_TOKEN"),
    http_client=DefaultHttpxClient(trust_env=False)
)

def run():
    # 1. Reset with a retry to ensure the server is awake
    for _ in range(3):
        try:
            requests.post("http://localhost:7860/reset", timeout=5)
            break
        except:
            time.sleep(2)

    # 2. Get the AI decision
    try:
        completion = client.chat.completions.create(
            model="Qwen/Qwen2.5-72B-Instruct",
            messages=[
                {"role": "system", "content": "You are a crisis manager. Respond with a JSON action."},
                {"role": "user", "content": "The situation is escalating. What is the next step?"}
            ]
        )
        decision = completion.choices[0].message.content
    except Exception as e:
        print(f"OpenAI Call Failed: {e}")
        return

    # 3. Step the environment
    try:
        requests.post(
            "http://localhost:7860/step", 
            json={"action": {"decision": decision}},
            timeout=5
        )
    except Exception as e:
        print(f"Step failed: {e}")

if __name__ == "__main__":
    run()
