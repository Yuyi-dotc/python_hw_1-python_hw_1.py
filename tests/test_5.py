from python_hw_1 import longest_common_prefix


def test_example1():
    assert longest_common_prefix(["flower", "flow", "flight"]) == "fl"


def test_example2():
    assert longest_common_prefix(["test", "test", "test"]) == "test"


def test_example3():
    assert longest_common_prefix(["test1", "test2", "test1"]) == "test"


def test_example4():
    assert longest_common_prefix(["test1"]) == "test1"


def test_example5():
    assert longest_common_prefix(["a", "b"]) == ""


def test_example6():
    assert longest_common_prefix(["aa", "aaa", "aaaa", "ab"]) == "a"


def test_example7():
    assert longest_common_prefix(["aa", "test", "test", "test"]) == ""
