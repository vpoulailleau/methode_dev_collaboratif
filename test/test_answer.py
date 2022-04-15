def inc(x):
    return x + 1


def test_answer():
    assert inc(3) == 5

def test_inc():
    assert inc(3) == 4

def test_int():
    assert inc(7) == 7

def test_str():
    assert inc(7) == "7"