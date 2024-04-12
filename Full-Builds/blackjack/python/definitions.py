from collections import namedtuple
import sys
from typing import Any
import os

class drawable_t(object):
    def __init__(self, position: tuple[float,float], color: tuple[int,int,int], size: tuple[float,float]) -> None:
        self.xy: tuple[float, float] = position
        self.color: tuple[int, int, int] = color
        self.size: tuple[float, float] = size

class event_t(object):
    def __init__(self, name: int, args: list[Any]) -> None:
        self.name: int = name
        self.args: dict[str, Any] = args
    
def drawable_f(object: dict) -> drawable_t:
    return drawable_t(tuple(object['xy']), tuple(object['color']), tuple(object['size']))

def c_dir():
    return os.path.dirname(__file__)

def exists(file: str):
    return os.path.exists(os.path.join(c_dir(), file))

def read_pipe() -> str:
    data = ""
    while True:
        byte = sys.stdin.read(1)
        if byte == "\n":
            return data
        data += byte

def write_pipe(string: str) -> bool:
    try:
        sys.stdout.write(string + "\n")
        sys.stdout.flush()
    except:
        return False

def close() -> None:
    write_pipe("quit")
    
def print(msg: Any, end="\n"):
    sys.stderr.write(str(msg) + end)