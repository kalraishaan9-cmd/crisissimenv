class CrisisGrader:
    def __init__(self):
        pass

    def check_termination(self, state_manager):
        state = state_manager.state

        if state["stability"] <= 0:
            return True
        if state["stability"] >= 100:
            return True
        if state["ticks"] >= 20:
            return True

        return False