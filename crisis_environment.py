import json
import os
from models import CrisisAction, CrisisObservation

class CrisisEnvironment:
    def __init__(self, task_id="phishing_scam"):
        # Expects tasks.json in the same root directory
        with open("tasks.json", "r") as f:
            self.tasks = json.load(f)
        self.task_id = task_id
        self.config = self.tasks.get(task_id, self.tasks["phishing_scam"])
        self.reset()

    def reset(self):
        self.current_threat = 1.0
        self.history = []
        self.done = False
        return CrisisObservation(
            scenario=self.config["scenario"],
            threat_level=self.current_threat,
            history=self.history
        )

    def step(self, action: CrisisAction):
        if self.done:
            return self.state(), 0.0, True, {"msg": "Episode ended"}

        # Keyword matching grader
        matches = [k for k in self.config["keywords"] if k.lower() in action.decision.lower()]
        unique_matches = [m for m in matches if m not in [h.lower() for h in self.history]]
        
        reward = len(unique_matches) * 0.15
        self.current_threat = max(0.0, self.current_threat - (len(unique_matches) * 0.2))
        
        self.history.append(action.decision)
        
        if self.current_threat <= 0 or len(self.history) >= 8:
            self.done = True
            if self.current_threat <= 0:
                reward += 0.2
        
        return self.state(), round(reward, 2), self.done, {}

    def state(self):
        return CrisisObservation(
            scenario=self.config["scenario"],
            threat_level=round(self.current_threat, 2),
            history=self.history
        )
