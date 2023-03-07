import pytest
from io import StringIO

from src.cli.cli import JabberwockyCLI
from run import main
from src.containers.container_manager_client import ContainerManagerClient

@pytest.fixture(scope="session")
def out_stream() -> StringIO:
    yield StringIO()

@pytest.fixture(scope="session")
def cli(out_stream) -> JabberwockyCLI:
    main()
    cur_cli = JabberwockyCLI(out_stream=out_stream)
    cur_cli.container_manager = ContainerManagerClient()
    yield cur_cli
    cur_cli.parse_cmd(['server-halt'])
