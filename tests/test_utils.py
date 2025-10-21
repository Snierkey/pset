import pytest
from pathlib import Path
from pset.utils import file_ops, git, venv

def test_file_ops():
    with pytest.raises(FileNotFoundError):
        file_ops.read_file('nonexistent.txt')
