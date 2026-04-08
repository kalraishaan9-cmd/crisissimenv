from pydantic import BaseModel, Field
from typing import List, Optional

class CrisisAction(BaseModel):
    decision: str = Field(..., description="Action taken by the responder")

class CrisisObservation(BaseModel):
    scenario: str
    threat_level: float
    history: List[str]
    last_action_error: Optional[str] = None