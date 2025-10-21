from pathlib import Path

def create_directory(path):
    Path(path).mkdir(parents=True, exist_ok=True)

def write_file(path, content):
    with open(path, 'w') as f:
        f.write(content)

def read_file(path):
    with open(path, 'r') as f:
        return f.read()
