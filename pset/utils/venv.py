import subprocess
import sys
from pathlib import Path

def create_venv(path):
    venv_path = path / "venv"
    try:
        subprocess.run([sys.executable, "-m", "venv", str(venv_path)], check=True, capture_output=True)
    except subprocess.CalledProcessError:
        pass
