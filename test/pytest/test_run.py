import pytest

from src.cli.cli import JabberwockyCLI

from test_common import send_cmd_to_cli, MyStream

@pytest.mark.depends(on=['test_install'])
def test_run_whoami(out_stream: MyStream, cli: JabberwockyCLI, ct_container: None):
    """
    Ensures that the run command works by running whoami on the ct container
    """
    s = send_cmd_to_cli(cli, out_stream, ["run", "ct", "whoami"])
    assert s == "root\n"
