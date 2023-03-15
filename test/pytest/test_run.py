import pytest

from src.cli.cli import JabberwockyCLI

from test_common import send_cmd_to_cli

@pytest.mark.depends(on=['test_install'])
def test_run_whoami(out_stream, cli, ct_container):
    s = send_cmd_to_cli(cli, out_stream, ["run", "ct", "whoami"])
    assert s == "root\n"
