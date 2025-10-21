import pytest
from click.testing import CliRunner
from pset.commands import create, build, publish, init, install

def test_create_command():
    runner = CliRunner()
    with runner.isolated_filesystem():
        result = runner.invoke(create, ['testpkg', '--author', 'Test Author'])
        assert result.exit_code == 0
        assert 'Package testpkg created successfully' in result.output
