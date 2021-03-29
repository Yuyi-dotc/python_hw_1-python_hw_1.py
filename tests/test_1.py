import pytest

from python_hw_1 import get_hello_world


class Case:
    def __init__(self, name: str, expected: str):
        self._name = name
        self.expected = expected

    def __str__(self):
        return "test_{}".format(self._name)


TEST_CASES = [Case(name="basic", expected="Hello, world!")]


@pytest.mark.parametrize("test_case", TEST_CASES, ids=lambda c: str(c))
def test_hello_world(test_case: Case):
    answer = get_hello_world()
    assert answer == test_case.expected
