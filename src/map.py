from src.game import init_game
from io import StringIO 
from contextlib import redirect_stdout



def get_map(rand):
    f = StringIO()
    with redirect_stdout(f):
        init_game(rand)
    return f.getvalue()
