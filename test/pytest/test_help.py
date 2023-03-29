from time import sleep
from io import StringIO
import pytest

from src.cli.cli import JabberwockyCLI

from test_common import send_cmd_to_cli, MyStream

def test_help(out_stream: MyStream, cli: JabberwockyCLI) -> None:
    """
    Ensures that the help command is working
    """
    out = send_cmd_to_cli(cli, out_stream, ["help"])
    assert out.startswith("Usage:")
