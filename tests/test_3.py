from typing import Mapping, Union

import pytest

from python_hw_1 import get_fizz_buzz


class Case(object):
    def __init__(self, name: str, n: int, expected: Mapping[int, Union[int, str]]):
        self._name = name
        self.n = n
        self.expected = expected

    def __str__(self):
        return "test_{}".format(self._name)


TEST_CASES = [
    Case(name="test_zero_element", n=1, expected={0: 1}),
    Case("test_first_three_elements", n=3, expected={0: 1, 1: 2, 2: "Fizz"}),
    Case(
        name="check_fizz",
        n=100,
        expected={i - 1: "Fizz" for i in range(3, 101, 3) if i % 15 != 0},
    ),
]


@pytest.mark.parametrize("test_case", TEST_CASES, ids=lambda c: str(c))
def test_get_fizz_buzz(test_case: Case):
    fizz_buzz_list = get_fizz_buzz(test_case.n)
    assert len(fizz_buzz_list) == test_case.n
    for key, value in test_case.expected.items():
        assert fizz_buzz_list[key] == value
