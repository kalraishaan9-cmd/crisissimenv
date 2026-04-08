from pydantic import BaseModel


class CrisisEvent(BaseModel):
    type: str
    severity: float
    affected_population: int
    spread_probability: float
    infrastructure_impact: float