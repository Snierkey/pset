import click
import subprocess
import sys
from pathlib import Path

@click.command()
@click.argument('package')
@click.option('--dev', is_flag=True, help='Install as development dependency')
@click.option('--editable', '-e', is_flag=True, help='Install in editable mode')
def install(package, dev, editable):
    try:
        if editable:
            subprocess.run(["pip", "install", "-e", package], check=True)
        elif dev:
            subprocess.run(["pip", "install", package], check=True)
            with open("requirements-dev.txt", "a") as f:
                f.write(f"\n{package}")
        else:
            subprocess.run(["pip", "install", package], check=True)
            with open("requirements.txt", "a") as f:
                f.write(f"\n{package}")
        
        click.echo(f"Package {package} installed successfully")
    except subprocess.CalledProcessError as e:
        click.echo(f"Installation failed: {e}")
        sys.exit(1)
