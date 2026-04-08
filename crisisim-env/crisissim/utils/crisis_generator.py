import numpy as np
from ..models import CrisisEvent


class CrisisGenerator:
    def __init__(self):
        self.types = ["flood", "fire", "earthquake", "pandemic"]

    def generate_crisis(self):
        crisis_type = np.random.choice(self.types)

        return CrisisEvent(
            type=crisis_type,
            severity=float(np.random.uniform(0.2, 0.9)),
            affected_population=int(np.random.uniform(3000, 20000)),
            spread_probability=float(np.random.uniform(0.1, 0.7)),
            infrastructure_impact=float(np.random.uniform(0.1, 0.8)),
        ).dict()