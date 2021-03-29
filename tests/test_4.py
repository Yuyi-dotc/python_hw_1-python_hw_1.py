import pytest

from python_hw_1 import get_value


class Case(object):
    def __init__(self, value: int, repeats: int, expected: int):
        self.value = value
        self.repeats = repeats
        self.expected = expected

    def __str__(self):
        return "test_{}_with_{}_repeats".format(self.value, self.repeats)


TEST_CASES = [
    Case(value=0, repeats=100, expected=0),
    Case(value=1, repeats=2, expected=121),
]


@pytest.mark.parametrize("test_case", TEST_CASES, ids=lambda c: str(c))
def test_kruchu_verchu(test_case: Case):
    combinations = get_value(test_case.value, test_case.repeats)
    assert combinations == test_case.expected
