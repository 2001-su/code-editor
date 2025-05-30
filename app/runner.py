import subprocess
import uuid
import os

def run_code_in_docker(code: str, user_input: str = "") -> dict:
    filename = f"/tmp/{uuid.uuid4().hex}.py"
    input_file = f"/tmp/{uuid.uuid4().hex}.txt"

    try:
        with open(filename, "w") as f:
            f.write(code)
        with open(input_file, "w") as f:
            f.write(user_input)

        result = subprocess.run(
            ["python", filename],
            input=open(input_file).read(),
            capture_output=True,
            text=True,
            timeout=5
        )

        return {
            "output": result.stdout,
            "error": result.stderr
        }
    except Exception as e:
        return {
            "output": "",
            "error": str(e)
        }
    finally:
        try:
            os.remove(filename)
            os.remove(input_file)
        except:
            pass
