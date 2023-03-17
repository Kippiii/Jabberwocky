import pytest
from pathlib import Path

from src.cli.cli import JabberwockyCLI

from test_common import send_cmd_to_cli, gen_random_local_file, gen_random_str, check_files_equal, MyStream

@pytest.mark.depends(on=['test_install'])
def test_put_get(out_stream: MyStream, cli: JabberwockyCLI, ct_container: None) -> None:
    """
    Ensures that file put and get work by sending a file to ct and getting it out
    """
    # Generate a random file
    start_file: Path = Path("/app/container_manager") / gen_random_str()
    gen_random_local_file(start_file)

    # Send random file to container
    container_file: Path = Path("/root") / gen_random_str()
    send_cmd_to_cli(cli, out_stream, ['send-file', 'ct', str(start_file), str(container_file)])

    # Get random file from container
    end_file: Path = Path("/app/container_manager") / gen_random_str()
    assert start_file != end_file
    send_cmd_to_cli(cli, out_stream, ['get-file', 'ct', str(container_file), str(end_file)])

    # Ensure files are equal
    assert check_files_equal(start_file, end_file)
