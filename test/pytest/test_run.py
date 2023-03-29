import pytest

from src.cli.cli import JabberwockyCLI

from test_common import send_cmd_to_cli, MyStream

def test_run_whoami(out_stream: MyStream, cli: JabberwockyCLI, ct_container: None):
    """
    Ensures that the run command works by running whoami on the ct container
    """
    s = send_cmd_to_cli(cli, out_stream, ["run", "ct", "whoami"])
    assert s == "root\n"

def test_run_fail_command(out_stream: MyStream, cli: JabberwockyCLI, ct_container: None) -> None:
    """
    Tests running a non-existent command
    """
    s = send_cmd_to_cli(cli, out_stream, ['run', 'ct', 'nonexistent'])
    assert 'nonexistent: not found' in s
