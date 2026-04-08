import numpy as np
from .utils.state_manager import StateManager
from .utils.crisis_generator import CrisisGenerator
from .utils.reward import RewardFunction
from .tasks.graders import CrisisGrader


class CrisisSimEnv:
    def __init__(self):
        self.generator = CrisisGenerator()
        self.state_manager = StateManager()
        self.reward_fn = RewardFunction()
        self.grader = CrisisGrader()

        self.current_crisis = None
        self.done = False

    def reset(self):
        self.current_crisis = self.generator.generate_crisis()
        self.state_manager.initialize(self.current_crisis)
        self.done = False
        return self.state_manager.get_state()

    def step(self, action):
        if self.done:
            raise RuntimeError("Environment already finished. Call reset().")

        state_update = self.state_manager.apply_action(action)
        reward = self.reward_fn.compute(self.state_manager, state_update)
        self.done = self.grader.check_termination(self.state_manager)

        next_state = self.state_manager.get_state()
        info = {"crisis_type": self.current_crisis['type']}

        return next_state, reward, self.done, info

    def state(self):
        return self.state_manager.get_state()