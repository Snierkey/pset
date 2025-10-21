import click
import subprocess
import sys
from pathlib import Path
from ..utils.git import init_git
from ..utils.venv import create_venv

@click.command()
@click.option('--git/--no-git', default=True, help='Initialize git repository')
@click.option('--venv/--no-venv', default=True, help='Create virtual environment')
def init(git, venv):
    current_dir = Path.cwd()
    
    if (current_dir / "setup.py").exists() or (current_dir / "pyproject.toml").exists():
        click.echo("This directory already appears to be a Python package")
        sys.exit(1)
    
    if git:
        init_git(current_dir)
    
    if venv:
        create_venv(current_dir)
    
    click.echo("Project initialized successfully")
