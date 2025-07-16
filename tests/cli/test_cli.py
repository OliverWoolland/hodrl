from click.testing import CliRunner
from hodrl.cli import click_entrypoint

def test_hello_world(all_assets):
  runner = CliRunner()
  result = runner.invoke(click_entrypoint, ["asset", "ls"])
  print(result)
                         
  assert result.exit_code == 0
  assert result.output == f"{all_assets}\n"
