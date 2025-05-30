from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import subprocess

app = FastAPI()

# Update this list with your actual frontend URL from Vercel
origins = [
    "https://code-editor-fastapi-32gnuly1c-sushma-sharons-projects.vercel.app",  # <-- Replace with your real frontend URL
    "http://localhost:3000",              # for local development
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Restrict to your frontend origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Backend is running"}

@app.post("/run")
def run_code(code: str):
    try:
        # Run the code safely in a subprocess (you can sandbox this better)
        result = subprocess.run(["python", "-c", code], capture_output=True, text=True, timeout=5)
        return {
            "output": result.stdout,
            "error": result.stderr
        }
    except Exception as e:
        return {"error": str(e)}

