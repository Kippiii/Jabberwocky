import pytest
import json
import shutil

from src.cli.cli import JabberwockyCLI

from test_common import send_cmd_to_cli, MyStream


def test_build_x86(out_stream: MyStream, cli: JabberwockyCLI) -> None:
    """
    Tests building with x86_64
    Also tests installing gdb and python deb package
    """
    send_cmd_to_cli(cli, out_stream, ["build-init", "x86_building"])

    shutil.copyfile("/share/python3.9_3.9.2-1_amd64.deb", "x86_building/packages/python3.9_3.9.2-1_amd64.deb")
    with open("x86_building/manifest.json") as f:
        manifest: dict = json.load(f)
    manifest["arch"] = "x86_64"
    manifest["aptpkgs"] = "gdb"
    with open("x86_building/manifest.json", "w") as f:
        json.dump(manifest, f)

    send_cmd_to_cli(cli, out_stream, ["build", "x86_building"])

    send_cmd_to_cli(
        cli,
        out_stream,
        ["install", "x86_building/build/jcontainer.tar.gz", "x86_built"],
    )
    send_cmd_to_cli(cli, out_stream, ["start", "x86_built"])
    try:
        send_cmd_to_cli(
            cli,
            out_stream,
            ["run", "x86_built", "gdb", "-o", "hello.o", "/share/hello_world.c"],
        )
        s = send_cmd_to_cli(cli, out_stream, ["run", "x86_built", "./hello.o"])
        assert s == "Hello World\n"
        s = send_cmd_to_cli(
            cli, out_stream, ["run", "x86_built", "python", "hello_world.py"]
        )
        assert s == "Hello World\n"
    finally:
        send_cmd_to_cli(cli, out_stream, ["stop", "x86_built"])
        send_cmd_to_cli(cli, out_stream, ["delete", "x86_built"])


def test_build_arm(out_stream: MyStream, cli: JabberwockyCLI) -> None:
    """
    Tests building with arm
    """
    send_cmd_to_cli(cli, out_stream, ["build-init", "arm_building"])

    with open("arm_building/manifest.json") as f:
        manifest: dict = json.load(f)
    manifest["arch"] = "aarch64"
    with open("arm_building/manifest.json", "w") as f:
        json.dump(manifest, f)

    send_cmd_to_cli(cli, out_stream, ["build", "arm_building"])

    send_cmd_to_cli(
        cli,
        out_stream,
        ["install", "arm_building/build/jcontainer.tar.gz", "arm_built"],
    )
    send_cmd_to_cli(cli, out_stream, ["start", "arm_built"])
    s = send_cmd_to_cli(cli, out_stream, ["run", "arm_built", "whoami"])
    assert s == "root\n"
    send_cmd_to_cli(cli, out_stream, ["stop", "arm_built"])
    send_cmd_to_cli(cli, out_stream, ["delete", "arm_built"])


def test_build_mips(out_stream: MyStream, cli: JabberwockyCLI) -> None:
    """
    Tests building with mips
    """
    send_cmd_to_cli(cli, out_stream, ["build-init", "mips_building"])

    with open("mips_building/manifest.json") as f:
        manifest: dict = json.load(f)
    manifest["arch"] = "aarch64"
    with open("mips_building/manifest.json", "w") as f:
        json.dump(manifest, f)

    send_cmd_to_cli(cli, out_stream, ["build", "mips_building"])

    send_cmd_to_cli(
        cli,
        out_stream,
        ["install", "mips_building/build/jcontainer.tar.gz", "mips_built"],
    )
    send_cmd_to_cli(cli, out_stream, ["start", "mips_built"])
    s = send_cmd_to_cli(cli, out_stream, ["run", "mips_built", "whoami"])
    assert s == "root\n"
    send_cmd_to_cli(cli, out_stream, ["stop", "mips_built"])
    send_cmd_to_cli(cli, out_stream, ["delete", "mips_built"])
