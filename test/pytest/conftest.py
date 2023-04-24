import pytest

from src.cli.cli import JabberwockyCLI
from run import main

from test_common import send_cmd_to_cli, MyStream


@pytest.fixture(scope="session")
def out_stream() -> MyStream:
    """
    The output stream that the cli sends to
    """
    yield MyStream(1)


@pytest.fixture(scope="session")
def in_stream() -> MyStream:
    """
    The input stream that the cli takes from
    """
    yield MyStream(0)


@pytest.fixture(scope="session")
def cli(out_stream: MyStream, in_stream: MyStream) -> JabberwockyCLI:
    """
    An instance of the cli
    """
    main()
    cur_cli = JabberwockyCLI(out_stream=out_stream, in_stream=in_stream)
    yield cur_cli
    try:
        cur_cli.parse_cmd(["server-halt"])
    finally:
        with open("/root/.containers/server.log") as f:
            print(f.read())


@pytest.fixture(scope="session")
def ct_container(out_stream: MyStream, cli: JabberwockyCLI) -> None:
    """
    Represents starting the ct container
    """
    send_cmd_to_cli(cli, out_stream, ["install", "/share/ct.tar.bz2", "ct"])
    send_cmd_to_cli(cli, out_stream, ["start", "ct"])
    yield None
    send_cmd_to_cli(cli, out_stream, ["stop", "ct"])
