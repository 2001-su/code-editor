from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import subprocess

app = FastAPI()

# Your frontend URLs
origins = [
    "https://code-editor-fastapi-32gnuly1c-sushma-sharons-projects.vercel.app",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Backend is running"}

class CodeRequest(BaseModel):
    code: str
    input: str = ""  # default empty input

@app.post("/run")
def run_code(request: CodeRequest):
    try:
        # Run the code, provide input via stdin
        result = subprocess.run(
            ["python", "-c", request.code],
            input=request.input,
            capture_output=True,
            text=True,
            timeout=5
        )
        return {
            "output": result.stdout,
            "error": result.stderr
        }
    except Exception as e:
        return {"error": str(e)}
