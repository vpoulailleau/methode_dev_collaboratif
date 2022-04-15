from src.game import init_game
from io import StringIO
from contextlib import redirect_stdout

import sys


class Capturing(list):
    def __enter__(self):
        self._stdout = sys.stdout
        sys.stdout = self._stringio = StringIO()
        return self

    def __exit__(self, *args):
        self.extend(self._stringio.getvalue().splitlines())
        del self._stringio  # free up some memory
        sys.stdout = self._stdout


class Map:
    def __init__(self) -> None:
        pass


def get_map(rand):
    f = StringIO()
    with redirect_stdout(f):
        init_game(rand)
    return f.getvalue()


def get_map_with_capturing(rand):
    with Capturing() as map:
        init_game(rand)
    return map


def create_grid(map):
    pass
