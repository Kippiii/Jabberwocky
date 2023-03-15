from time import sleep
from io import StringIO
import pytest

from src.cli.cli import JabberwockyCLI

from test_common import send_cmd_to_cli

def test_help(out_stream, cli) -> None:
    cli.parse_cmd(["help"])
    out = out_stream.getvalue()
    assert out.startswith("Usage:")
