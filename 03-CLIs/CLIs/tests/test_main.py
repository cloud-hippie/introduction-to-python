from CLIs.main import cli, configure

from click.testing import CliRunner


def test_hello_world():
  runner = CliRunner()
  result = runner.invoke(configure,['--count', '1', '--name', 'John'])
  assert result.exit_code == 0
  assert result.output == 'Hello John!\n'