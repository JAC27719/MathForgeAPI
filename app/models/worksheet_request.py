from typing import List
from pydantic import BaseModel
from models.worksheet_question import WorksheetQuestion

class WorksheetRequest(BaseModel):
    title: str
    questions: List[WorksheetQuestion]