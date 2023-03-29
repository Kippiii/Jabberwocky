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
    """
    Custom stream object for running tests

    :param buffer: The conent currently saved in the stream
    """
    buffer: str
    num: int

    def __init__(self, num: int) -> None:
        self.buffer = ""
        self.num = num

    def read(self, n: int = 9999999999) -> str:
        """
        Get n bytes from the stream

        :param n: The number of bytes to read
        """
        n = min(n, len(self.buffer))
        ret_val = self.buffer[:n]
        self.buffer = self.buffer[n:]
        return ret_val

    def readline(self) -> str:
        """
        Read until the next newline
        """
        ret_val: str = ""
        while len(self.buffer) > 0:
            c: str = self.buffer[0]
            self.buffer = self.buffer[1:]
            if c == '\n':
                break
            ret_val += c
        if ret_val == "":
            ret_val = "\0"
        return ret_val

    def write(self, s: str) -> None:
        """
        Write a string to the buffer

        :param s: The string being written the buffer
        """
        self.buffer += s

    def flush(self) -> None:
        """
        Flushes the stream
        """
        pass
    
    def fileno(self) -> int:
        return self.num

def send_cmd_to_cli(cli: JabberwockyCLI, out_stream: MyStream, cmd: List[str]) -> str:
    """
    Sends a command to the cli

    :param cli: cli: The instance of the cli
    :param out_stream: The stream the output is taken from
    :param cmd: The command being run
    """
    cli.parse_cmd(cmd)
    return out_stream.read()

def gen_random_local_file(path: Path, min_size: int = 0, max_size: int = 16*1024*1024) -> None:
    """
    Generates a random file in the file system

    :param path: The path where the random file is generated
    :param min_size: The smallest size of the file
    :param max_size: The largest size of the file
    """
    size: int = random.randrange(min_size, max_size)
    with open(str(path), "wb") as f:
        f.write(os.urandom(size))

def gen_random_str(min_length: int = 1, max_length: int = 32) -> str:
    """
    Generates a random string

    :param min_length: The smallest length of the string
    :param max_length: The largest length of the string
    """
    length: int = random.randrange(min_length, max_length)
    return ''.join(random.choices(string.ascii_lowercase, k=length))  # TODO All file names?

def check_files_equal(path1: Path, path2: Path) -> bool:
    """
    Ensures that two files are equal

    :param path1: Path to the first file
    :param path2: Path to the second file
    """
    return filecmp.cmp(str(path1), str(path2))

def get_repo_server_ip() -> str:
    """
    Gets the ip of the repo server
    """
    with open("/share/repo_server.ip") as f:
        return f.read().strip()
