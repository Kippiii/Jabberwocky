import pytest
import shutil
from pathlib import Path

from test_common import send_cmd_to_cli, get_repo_server_ip

def test_download(out_stream, in_stream, cli) -> None:
    send_cmd_to_cli(cli, out_stream, ["add-repo", f"http://{get_repo_server_ip()}:5000"])
    in_stream.write("y\n")
    send_cmd_to_cli(cli, out_stream, ["download", "ct.tar.bz2", "downloaded"])
    send_cmd_to_cli(cli, out_stream, ["start", "downloaded"])
    try:
        s = send_cmd_to_cli(cli, out_stream, ["run", "downloaded", "whoami"])
        assert s == "root"
    finally:
        send_cmd_to_cli(cli, out_stream, ["stop", "downloaded"])
        send_cmd_to_cli(cli, out_stream, ["delete", "downloaded"])

def test_upload(out_stream, in_stream, cli, ct_container) -> None:
    send_cmd_to_cli(cli, out_stream, ["stop", "ct"])
    try:
        in_stream.write("admin\nadminadmin\n")
        send_cmd_to_cli(cli, out_stream, ["upload", "ct", f"http://{get_repo_server_ip()}:5000"])

        assert Path("ct.tar.gz").is_file(), "File not created!"
        with tarfile.open("ct.tar.gz", "r:gz") as tar:
            names = tar.get_names()
            assert len(names) == 2, f"len({names}) != 2"
            assert "config.json" in names, "config.json not in archive"
            assert "hdd.qcow2" in names, "hdd.qcow2 not in archive"
    finally:
        send_cmd_to_cli(cli, out_stream, ["start", "ct"])
