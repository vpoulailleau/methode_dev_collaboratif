from src.map import get_map, get_map_with_capturing


def test_map_0():
    assert get_map(5) == get_map(5)


def test_map_1():
    assert get_map(4) != get_map(9)


def test_map_2():
    assert get_map_with_capturing(5) == get_map_with_capturing(5)


def test_map_3():
    assert get_map_with_capturing(4) != get_map_with_capturing(9)
