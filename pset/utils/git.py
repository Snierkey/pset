import subprocess
from pathlib import Path

def init_git(path):
    try:
        subprocess.run(["git", "init"], cwd=path, check=True, capture_output=True)
        subprocess.run(["git", "add", "."], cwd=path, check=True, capture_output=True)
        subprocess.run(["git", "commit", "-m", "Initial commit"], cwd=path, check=True, capture_output=True)
    except subprocess.CalledProcessError:
        pass
