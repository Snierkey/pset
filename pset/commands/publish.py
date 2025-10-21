import click
import subprocess
import sys
from pathlib import Path

@click.command()
@click.option('--repository', default='pypi', help='Repository to publish to')
@click.option('--username', help='Username for repository')
@click.option('--password', help='Password for repository')
@click.option('--test', is_flag=True, help='Publish to test repository')
def publish(repository, username, password, test):
    current_dir = Path.cwd()
    
    if not (current_dir / "dist").exists():
        click.echo("No dist directory found. Run 'pset build' first")
        sys.exit(1)
    
    cmd = ["python", "-m", "twine", "upload"]
    
    if test:
        cmd.extend(["--repository", "testpypi"])
    elif repository != "pypi":
        cmd.extend(["--repository", repository])
    
    if username:
        cmd.extend(["--username", username])
    if password:
        cmd.extend(["--password", password])
    
    cmd.append("dist/*")
    
    try:
        subprocess.run(cmd, check=True)
        click.echo("Package published successfully")
    except subprocess.CalledProcessError as e:
        click.echo(f"Publish failed: {e}")
        sys.exit(1)
