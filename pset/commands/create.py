import click
import os
import json
from pathlib import Path
from jinja2 import Template
from ..utils.file_ops import create_directory, write_file
from ..utils.git import init_git
from ..utils.venv import create_venv

@click.command()
@click.argument('name')
@click.option('--author', default='', help='Author name')
@click.option('--email', default='', help='Author email')
@click.option('--description', default='', help='Package description')
@click.option('--license', default='MIT', help='License type')
@click.option('--python-version', default='3.8', help='Minimum Python version')
@click.option('--git/--no-git', default=True, help='Initialize git repository')
@click.option('--venv/--no-venv', default=True, help='Create virtual environment')
def create(name, author, email, description, license, python_version, git, venv):
    package_dir = Path(name)
    
    if package_dir.exists():
        click.echo(f"Directory {name} already exists")
        sys.exit(1)
    
    create_directory(package_dir)
    create_directory(package_dir / name)
    create_directory(package_dir / "tests")
    create_directory(package_dir / "docs")
    
    context = {
        'name': name,
        'author': author,
        'email': email,
        'description': description,
        'license': license,
        'python_version': python_version,
        'version': '0.1.0'
    }
    
    template_dir = Path(__file__).parent.parent / "templates"
    
    with open(template_dir / "setup_py.j2") as f:
        template = Template(f.read())
        write_file(package_dir / "setup.py", template.render(**context))
    
    with open(template_dir / "pyproject_toml.j2") as f:
        template = Template(f.read())
        write_file(package_dir / "pyproject.toml", template.render(**context))
    
    with open(template_dir / "readme_md.j2") as f:
        template = Template(f.read())
        write_file(package_dir / "README.md", template.render(**context))
    
    with open(template_dir / "gitignore.j2") as f:
        template = Template(f.read())
        write_file(package_dir / ".gitignore", template.render())
    
    write_file(package_dir / name / "__init__.py", f'__version__ = "{context["version"]}"\n')
    
    with open(template_dir / "test_init.j2") as f:
        template = Template(f.read())
        write_file(package_dir / "tests" / "__init__.py", template.render())
    
    write_file(package_dir / "requirements.txt", "")
    write_file(package_dir / "requirements-dev.txt", "pytest\nblack\nflake8\nmypy")
    
    if git:
        init_git(package_dir)
    
    if venv:
        create_venv(package_dir)
    
    click.echo(f"Package {name} created successfully")
