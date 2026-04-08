import requests
import os

# Update this to your running Space URL
ENV_URL = "https://thelabsters-crisissimenv.hf.space"

def run_inference():
    print("[START]")
    # Reset environment
    res = requests.post(f"{ENV_URL}/reset")
    obs = res.json()
    print(f"[STEP] Scenario: {obs['scenario']}")

    # Mock Action
    action = {"decision": "I will reset all user passwords and notify the IT team."}
    res = requests.post(f"{ENV_URL}/step", json=action)
    data = res.json()
    
    print(f"[STEP] Reward: {data['reward']}")
    print(f"[END] Final Score: {data['reward']}")

if __name__ == "__main__":
    run_inference()