from fastapi import FastAPI
import models
from models.worksheet_question import WorksheetQuestion
from models.worksheet_request import WorksheetRequest

print("Using models version: ", models.version)

app = FastAPI()

@app.post("/generate")
async def generate_worksheet():
    wr = WorksheetRequest(title="Title", questions=[WorksheetQuestion(instructions="Instruction", difficulty="Difficulty", format="Format")])
    return wr

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)