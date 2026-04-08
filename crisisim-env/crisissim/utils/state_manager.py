import numpy as np


class StateManager:
    def __init__(self):
        self.state = {}

    def initialize(self, crisis):
        self.state = {
            "stability": 50,
            "crisis": crisis,
            "ticks": 0
        }

    def apply_action(self, action):
        decision = action.get("decision", "none")

        if decision == "analyze":
            self.state["stability"] += np.random.randint(1, 4)
        elif decision == "deploy":
            self.state["stability"] += np.random.randint(3, 7)
        else:
            self.state["stability"] -= np.random.randint(1, 3)

        self.state["stability"] = max(0, min(100, self.state["stability"]))

        self.state["ticks"] += 1

        return {"decision": decision}

    def get_state(self):
        return self.state