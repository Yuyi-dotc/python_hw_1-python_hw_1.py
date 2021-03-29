from python_hw_1 import is_perfect


def test_example1():
    assert not is_perfect(1)


def test_example2():
    assert is_perfect(6)


def test_example4():
    assert not is_perfect(20)


def test_example5():
    assert is_perfect(28)


def test_example6():
    assert is_perfect(496)


def test_example7():
    assert not is_perfect(1543)
