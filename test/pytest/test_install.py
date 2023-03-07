import pytest

from src.cli.cli import JabberwockyCLI

from test_common import cli, out_stream

def test_install_container_theory(out_stream, cli: JabberwockyCLI):
    cli.parse_cmd(["install", "./share/ct.tar.bz2", "ct"])
