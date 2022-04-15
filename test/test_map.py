from src.map import get_map


def test_map_0():
    assert get_map(5) == get_map(5)

def test_map_1():
    assert get_map(4) != get_map(9)