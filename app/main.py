from fastapi import FastAPI, Request
from pydantic import BaseModel
from .runner import run_code_in_docker

app = FastAPI()

class CodeRequest(BaseModel):
    code: str
    input: str = ""

@app.post("/run")
async def run_code(request: CodeRequest):
    result = run_code_in_docker(request.code, request.input)
    return result

@app.get("/")
async def root():
    return {"message": "Backend is running!"}
