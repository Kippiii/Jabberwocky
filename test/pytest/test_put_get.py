import pytest
import os
from pathlib import Path

from src.cli.cli import JabberwockyCLI
from src.containers.exceptions import InvalidPathError

from test_common import (
    send_cmd_to_cli,
    gen_random_local_file,
    gen_random_str,
    check_files_equal,
    MyStream,
)


def test_put_get(out_stream: MyStream, cli: JabberwockyCLI, ct_container: None) -> None:
    """
    Ensures that file put and get work by sending a file to ct and getting it out
    """
    # Generate a random file
    start_file: Path = Path("/app/container_manager") / gen_random_str()
    gen_random_local_file(start_file)

    # Send random file to container
    container_file: Path = Path("/root") / gen_random_str()
    send_cmd_to_cli(
        cli, out_stream, ["send-file", "ct", str(start_file), str(container_file)]
    )

    # Get random file from container
    end_file: Path = Path("/app/container_manager") / gen_random_str()
    assert start_file != end_file
    send_cmd_to_cli(
        cli, out_stream, ["get-file", "ct", str(container_file), str(end_file)]
    )

    # Ensure files are equal
    assert check_files_equal(start_file, end_file)


def test_get_empty_file(
    out_stream: MyStream, cli: JabberwockyCLI, ct_container: None
) -> None:
    """
    Creates an empty file and then gets it
    """
    # Touch an empty file on the container
    send_cmd_to_cli(cli, out_stream, ["run", "ct", "touch", "empty_file"])

    # Get the file
    send_cmd_to_cli(cli, out_stream, ["get-file", "ct", "empty_file"])

    # Check file exists
    assert os.path.exists("empty_file") and os.path.getsize("empty_file") == 0


def test_root_transfer(
    out_stream: MyStream, cli: JabberwockyCLI, ct_container: None
) -> None:
    """
    Test put and get file using ~
    """
    # Generate a random file
    filename: str = gen_random_str()
    start_file: Path = Path("/app/container_manager") / filename
    gen_random_local_file(start_file)

    # Send random file to container
    send_cmd_to_cli(cli, out_stream, ["send-file", "ct", str(start_file), "~"])

    # Get random file from container (assumes we aren't in home)
    send_cmd_to_cli(cli, out_stream, ["get-file", "ct", f"/root/{str(filename)}", "~"])

    # Ensure files are equal
    assert check_files_equal(start_file, Path("/root") / filename)


def test_send_file_no_exist(
    out_stream: MyStream, cli: JabberwockyCLI, ct_container: None
) -> None:
    """
    Tests a failure in sending a file to the container
    """
    try:
        send_cmd_to_cli(
            cli, out_stream, ["send-file", "ct", "file_does_not_exist", "file"]
        )
    except InvalidPathError:
        pass
    else:
        raise Exception("Invalid Path Error not raised")


def test_get_file_no_exist(
    out_stream: MyStream, cli: JabberwockyCLI, ct_container: None
) -> None:
    """
    Tests getting a file that does not exist
    """
    try:
        send_cmd_to_cli(
            cli, out_stream, ["get-file", "ct", "file_does_not_exist", "file"]
        )
    except InvalidPathError:
        pass
    else:
        raise Exception("Invalid Path Error not raised")


def test_send_file_invalid_dir(
    out_stream: MyStream, cli: JabberwockyCLI, ct_container: None
) -> None:
    """
    Tests sending a file to an invalid directory
    """
    # Generate a random file
    start_file: Path = Path("/app/container_manager") / gen_random_str()
    gen_random_local_file(start_file)

    # Send file to invalid directory
    try:
        send_cmd_to_cli(
            cli,
            out_stream,
            ["send-file", "ct", str(start_file), "invalid_directory/the_file"],
        )
    except InvalidPathError:
        pass
    else:
        raise Exception("Invalid Path Error not raised")


def test_get_file_invalid_dir(
    out_stream: MyStream, cli: JabberwockyCLI, ct_container: None
) -> None:
    """
    Tests getting a file to an invalid directory
    """
    # Generate a random file
    file_name: str = gen_random_str()
    start_file: Path = Path("/app/container_manager") / file_name
    gen_random_local_file(start_file)

    # Send file to container
    send_cmd_to_cli(cli, out_stream, ["send-file", "ct", str(start_file)])

    # Get file to invalid directory
    try:
        send_cmd_to_cli(
            cli, out_stream, ["get-file", "ct", file_name, "invalid_directory/the_file"]
        )
    except InvalidPathError:
        pass
    else:
        raise Exception("Invalid Path Error not raised")
