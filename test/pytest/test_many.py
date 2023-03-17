import pytest

from src.cli.cli import JabberwockyCLI

from test_common import send_cmd_to_cli, MyStream

def test_many(out_stream: MyStream, cli: JabberwockyCLI):
    """
    Ensures that five containers can be run at the same time
    """
    try:
        # Install all containers
        for i in range(5):
            send_cmd_to_cli(cli, out_stream, ["install", "/share/ct.tar.bz2", f"ct{i}"])

        # Start all containers
        for i in range(5):
            send_cmd_to_cli(cli, out_stream, ['start', f'ct{i}'])

        # Create files in each container
        for i in range(5):
            send_cmd_to_cli(cli, out_stream, ["run", f"ct{i}", "touch", f"file{i}"])

        # Ensure files are right for each container
        for i in range(5):
            s = send_cmd_to_cli(cli, out_stream, ["run", f"ct{i}", "ls"])
            assert s == f"file{i}"

    finally:
        # Stop all containers
        for i in range(5):
            send_cmd_to_cli(cli, out_strema, ["stop", f"ct{i}"])

        # Delete all containers
        for i in range(5):
            send_cmd_to_cli(cli, out_stream, ["delete", f"ct{i}"])