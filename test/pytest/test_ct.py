import pytest

from src.cli.cli import JabberwockyCLI

from test_common import send_cmd_to_cli, MyStream


def test_ct_gcc(out_stream: MyStream, cli: JabberwockyCLI, ct_container: None) -> None:
    """
    Ensures that sparc linux gcc is working in the ct container
    """
    try:
        send_cmd_to_cli(
            cli,
            out_stream,
            ["send-file", "ct", "/share/hello_world.c", "hello_world.c"],
        )
        send_cmd_to_cli(
            cli,
            out_stream,
            ["run", "ct", "sparc-linux-gcc", "-o", "hello.out", "hello_world.c"],
        )
        send_cmd_to_cli(cli, out_stream, ["run", "ct", "chmod", "u+x", "hello.out"])
        s = send_cmd_to_cli(cli, out_stream, ["run", "ct", "./hello.out"])
        assert s == "Hello World!\n"
    except AssertionError as exc:
        s = send_cmd_to_cli(cli, out_stream, ["run", "ct", "ls"])
        raise Exception(s) from exc
    finally:
        send_cmd_to_cli(
            cli, out_stream, ["run", "ct", "rm", "-rf", "hello_world.c", "hello.out"]
        )


def test_ct_java(out_stream: MyStream, cli: JabberwockyCLI, ct_container: None) -> None:
    """
    Ensures that java is installed and working in the ct container
    """
    try:
        send_cmd_to_cli(
            cli,
            out_stream,
            ["send-file", "ct", "/share/HelloWorld.java", "HelloWorld.java"],
        )
        send_cmd_to_cli(cli, out_stream, ["run", "ct", "javac", "HelloWorld.java"])
        s = send_cmd_to_cli(cli, out_stream, ["run", "ct", "java", "HelloWorld"])
        assert s == "Hello World!\n"
    finally:
        send_cmd_to_cli(
            cli,
            out_stream,
            ["run", "ct", "rm", "-rf", "HelloWorld.java", "HelloWorld.class"],
        )


def test_ct_sparc_asm(
    out_stream: MyStream, cli: JabberwockyCLI, ct_container: None
) -> None:
    """
    Ensures that sparc linux as and ld are working in the ct container
    """
    try:
        send_cmd_to_cli(
            cli,
            out_stream,
            ["send-file", "ct", "/share/hello_world.S", "hello_world.S"],
        )
        send_cmd_to_cli(
            cli,
            out_stream,
            ["run", "ct", "sparc-linux-as", "hello_world.S", "-o", "hello_world.o"],
        )
        send_cmd_to_cli(
            cli,
            out_stream,
            [
                "run",
                "ct",
                "sparc-linux-ld",
                "-o",
                "hello_world.out",
                "-dn",
                "-s",
                "hello_world.o",
            ],
        )
        s = send_cmd_to_cli(cli, out_stream, ["run", "ct", "./hello_world.out"])
        assert s == "Hello World!\n"
    finally:
        send_cmd_to_cli(
            cli,
            out_stream,
            [
                "run",
                "ct",
                "rm",
                "-rf",
                "hello_world.S",
                "hello_world.out",
                "hello_world.o",
            ],
        )
