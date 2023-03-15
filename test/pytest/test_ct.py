import pytest

from test_common import send_cmd_to_cli

def test_ct_gcc(out_stream, cli, ct_container) -> None:
    try:
        send_cmd_to_cli(cli, out_stream, ["put-file", "ct", "/share/hello_world.c", "hello_world.c"])
        send_cmd_to_cli(cli, out_stream, ["run", "ct", "sparc-linux-gcc", "hello_world.c", "-o", "hello_world.o"])
        s = send_cmd_to_cli(cli, out_stream, ["run", "ct", "./hello_world.o"])
        assert s == "Hello World!"
    finally:
        send_cmd_to_cli(cli, out_stream, ["run", "ct", "rm", "-rf", "hello_world.c", "hello_world.o"])

def test_ct_java(out_stream, cli, ct_container) -> None:
    try:
        send_cmd_to_cli(cli, out_stream, ["put-file", "ct", "/share/HelloWorld.java", "HelloWorld.java"])
        send_cmd_to_cli(cli, out_stream, ["run", "ct", "javac", "HelloWorld.java"])
        s = send_cmd_to_cli(cli, out_stream, ["run", "ct", "java", "HelloWorld"])
        assert s == "Hello World!"
    finally:
        send_cmd_to_cli(cli, out_stream, ["run", "ct", "rm", "-rf", "HelloWorld.java", "HelloWorld.class"])

def test_ct_sparc_asm(out_stream, cli, ct_container) -> None:
    try:
        send_cmd_to_cli(cli, out_stream, ["put-file", "ct", "/share/hello_world.S", "hello_world.S"])
        send_cmd_to_cli(cli, out_stream, ["run", "ct", "sparc-linux-as", "hello_world.S"])
        send_cmd_to_cli(cli, out_stream, ["run", "ct", "ld", "-o", "hello_world.out", "-dn", "-s", "hello_world.o"])
        s = send_cmd_to_cli(cli, out_stream, ["run", "ct", "./hello_world.out"])
        assert s == "Hello World!"
    finally:
        send_cmd_to_cli(cli, out_stream, ["run", "ct", "rm", "rf", "hello_world.S", "hello_world.out", "hello_world.o"])
