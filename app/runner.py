import docker
import uuid

client = docker.from_env()

def run_code_in_docker(code: str, user_input: str = "") -> dict:
    container_name = f"code-runner-{uuid.uuid4().hex[:8]}"
    try:
        # Prepare Python command
        code_command = f'echo """{code}""" > main.py && echo "{user_input}" > input.txt && cat input.txt | python main.py'

        container = client.containers.run(
            image="python:3.11-alpine",
            command=["sh", "-c", code_command],
            name=container_name,
            detach=True,
            stdin_open=True,
            tty=True,
            network_disabled=True,
            mem_limit="100m"
        )

        result = container.wait(timeout=10)
        logs = container.logs(stdout=True, stderr=True).decode()

        container.remove()
        return {"output": logs, "error": ""}
    except Exception as e:
        try:
            container.remove(force=True)
        except:
            pass
        return {"output": "", "error": str(e)}
