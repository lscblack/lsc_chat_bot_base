from fastapi import FastAPI
from pydantic import BaseModel
from bot import ask

app = FastAPI()

class Query(BaseModel):
    question: str

@app.post("/ask")
def ask_bot(query: Query):
    response = ask(query.question)
    return {"response": response}