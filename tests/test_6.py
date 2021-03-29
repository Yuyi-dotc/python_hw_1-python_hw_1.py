from python_hw_1 import password_strength


def test_example1():
    assert password_strength("Anna12345") == "weak"


def test_example2():
    assert password_strength("Anna_sdfajsdfaJJKJKLKJ:JK432342") == "weak"


def test_example3():
    assert password_strength("qW3") == "weak"


def test_example4():
    assert password_strength("qwE3qqqq") == "strong"


def test_example5():
    assert password_strength("qW3qW3qW3qW3") == "weak"


def test_example6():
    assert password_strength("dsfJJKLJKsdfsdfsdfNJHJHHKJKJH_*") == "weak"
