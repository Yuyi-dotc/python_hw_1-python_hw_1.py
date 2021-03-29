import pytest

from python_hw_1 import get_nearest_happy_ticket


class Case(object):
    def __init__(self, current_ticket, expected):
        self.current_ticket = current_ticket
        self.expected = expected

    def __str__(self):
        return "test_{}".format(self.current_ticket)


TEST_CASES = [
    Case(current_ticket="228419", expected="228417"),
    Case(current_ticket="225817", expected="225810"),
    Case(current_ticket="224900", expected="224800"),
    Case(current_ticket="222518", expected="222510"),
    Case(current_ticket="224526", expected="224530"),
    Case(current_ticket="221277", expected="221302"),
    Case(current_ticket="223517", expected="223520"),
    Case(current_ticket="222537", expected="222510"),
    Case(current_ticket="223160", expected="223160"),
    Case(current_ticket="223496", expected="223502"),
    Case(current_ticket="221369", expected="221401"),
    Case(current_ticket="226591", expected="226604"),
    Case(current_ticket="226342", expected="226343"),
    Case(current_ticket="227012", expected="227029"),
    Case(current_ticket="224928", expected="225009"),
    Case(current_ticket="000000", expected="000000"),
    Case(current_ticket="999998", expected="999999"),
]


@pytest.mark.parametrize("test_case", TEST_CASES)
def test_nearest_happy_ticket(test_case):
    nearest_happy_ticket = get_nearest_happy_ticket(test_case.current_ticket)
    assert nearest_happy_ticket == test_case.expected
