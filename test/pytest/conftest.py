import pytest

from src.cli.cli import JabberwockyCLI
from run import main

from test_common import send_cmd_to_cli, MyStream

@pytest.fixture(scope="session")
def out_stream() -> MyStream:
    yield MyStream()

@pytest.fixture(scope="session")
def in_stream() -> MyStream:
    yield MyStream()

@pytest.fixture(scope="session")
def cli(out_stream, in_stream) -> JabberwockyCLI:
    main()
    cur_cli = JabberwockyCLI(out_stream=out_stream, in_stream=in_stream)
    yield cur_cli
    try:
        cur_cli.parse_cmd(['server-halt'])
    finally:
        with open('/root/.containers/server.log') as f:
            print(f.read())

@pytest.fixture(scope="session")
def ct_container(out_stream, cli: JabberwockyCLI) -> None:
    send_cmd_to_cli(cli, out_stream, ["install", "/share/ct.tar.bz2", "ct"])
    send_cmd_to_cli(cli, out_stream, ['start', 'ct'])
    yield None
    send_cmd_to_cli(cli, out_stream, ['stop', 'ct'])