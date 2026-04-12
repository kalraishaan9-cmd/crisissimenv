import numpy as np

class CrisisEnvironment:
    def __init__(self):
        self.state = None
        self.steps = 0

    def reset(self):
        self.state = {"status": "initial", "threat_level": 5}
        self.steps = 0
        return self.state

    def step(self, action):
        self.steps += 1
        # Basic logic: reward is based on action presence
        reward = 1.0 if action else 0.0
        self.state = {"status": "ongoing", "threat_level": max(0, 5 - self.steps)}
        done = self.steps >= 5
        return self.state, reward, done, {}
