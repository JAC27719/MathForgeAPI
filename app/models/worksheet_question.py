from pydantic import BaseModel

class WorksheetQuestion(BaseModel):
    instructions: str
    difficulty: str
    format: str