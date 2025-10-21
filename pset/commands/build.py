import click
import subprocess
import sys
from pathlib import Path

@click.command()
@click.option('--clean', is_flag=True, help='Clean build directory before building')
def build(clean):
    current_dir = Path.cwd()
    
    if not (current_dir / "setup.py").exists() and not (current_dir / "pyproject.toml").exists():
        click.echo("No setup.py or pyproject.toml found. Are you in a package directory?")
        sys.exit(1)
    
    if clean:
        dist_dir = current_dir / "dist"
        if dist_dir.exists():
            import shutil
            shutil.rmtree(dist_dir)
            click.echo("Cleaned dist directory")
    
    try:
        if (current_dir / "pyproject.toml").exists():
            subprocess.run(["python", "-m", "build"], check=True)
        else:
            subprocess.run(["python", "setup.py", "sdist", "bdist_wheel"], check=True)
        click.echo("Build completed successfully")
    except subprocess.CalledProcessError as e:
        click.echo(f"Build failed: {e}")
        sys.exit(1)
