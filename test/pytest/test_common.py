import pytest
from pathlib import Path
from typing import List
import random
import os
import filecmp
import string

from src.cli.cli import JabberwockyCLI
from run import main
from src.containers.container_manager_client import ContainerManagerClient

class MyStream:
    buffer: str

    def __init__(self) -> None:
        self.buffer = ""
    def read(self, n: int = 9999999999) -> str:
        n = min(n, len(self.buffer))
        ret_val = self.buffer[:n]
        self.buffer = self.buffer[n:]
        return ret_val
    def readline(self) -> str:
        ret_val: str = ""
        while len(self.buffer) > 0:
            c: str = self.buffer[0]
            self.buffer = self.buffer[1:]
            if c == '\n':
                break
            ret_val += c
        return ret_val
    def write(self, s: str) -> None:
        self.buffer += s
    def flush(self) -> None:
        pass

def send_cmd_to_cli(cli: JabberwockyCLI, out_stream, cmd: List[str]) -> str:
    cli.parse_cmd(cmd)
    return out_stream.read()

def gen_random_local_file(path: Path, min_size: int = 0, max_size: int = 16*1024*1024) -> None:
    size: int = random.randrange(min_size, max_size)
    with open(str(path), "wb") as f:
        f.write(os.urandom(size))

def gen_random_str(min_length: int = 1, max_length: int = 32) -> str:
    length: int = random.randrange(min_length, max_length)
    return ''.join(random.choices(string.ascii_lowercase, k=length))  # TODO All file names?

def check_files_equal(path1: Path, path2: Path) -> bool:
    return filecmp.cmp(str(path1), str(path2))

def get_repo_server_ip() -> str:
    with open("/share/repo_server.ip") as f:
        return f.read().strip()
