class RewardFunction:
    def compute(self, state_manager, update):
        stability = state_manager.state["stability"]
        ticks = state_manager.state["ticks"]

        reward = (stability / 100) - (ticks * 0.01)
        return float(reward)