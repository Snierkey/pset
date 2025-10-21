import click
import sys
from .commands import create, build, publish, init, install

@click.group()
@click.version_option()
def cli():
    pass

cli.add_command(create.create)
cli.add_command(build.build)
cli.add_command(publish.publish)
cli.add_command(init.init)
cli.add_command(install.install)

def main():
    cli()
