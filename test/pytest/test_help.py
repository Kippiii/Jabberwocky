from time import sleep
from io import StringIO
import pytest

from src.cli.cli import JabberwockyCLI

from test_common import cli, out_stream

def test_help(out_stream: StringIO, cli: JabberwockyCLI) -> None:
    cli.parse_cmd(["help"])
    out = out_stream.getvalue()
    assert out.startswith("Usage:")
