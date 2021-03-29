import pytest

from python_hw_1 import parse_color


def test_hex():
    assert parse_color("#AAaaaa") == [170, 170, 170]


def test_trivial():
    assert parse_color("rgb(1, 2, 3)") == [1, 2, 3]


def test_none():
    assert parse_color("#gggggg") is None


def test_mess():
    assert parse_color("brg(70, 71, 72)") == [71, 72, 70]


def test_spaces():
    assert parse_color("rgb(   255, 255,    255 )") == [255, 255, 255]


INPUTS = [
    "#aaaaaa",
    "rgb(1000, 2000, 3000)",
    "#gggggg",
    "text",
    "bgr(1%, 2, 4)",
    "bgr(10%, 100%,32%)",
    "rgb(1, 2, 3)",
    "rbg(1,2,3)",
    "grb(10, 11, 12)",
    "gbr(40, 50, 60)",
    "brg(70, 71, 72)",
    "bgr(1,2, 3)",
    "rgb(   255, 255,    255 )",
    "rbg(5%, 6%, 7%)",
    "1%, 1%, 1%",
    "1,1,1)",
]

OUTPUTS = [
    [170, 170, 170],
    None,
    None,
    None,
    None,
    [81, 255, 25],
    [1, 2, 3],
    [1, 3, 2],
    [11, 10, 12],
    [60, 40, 50],
    [71, 72, 70],
    [3, 2, 1],
    [255, 255, 255],
    [12, 17, 15],
    None,
    None,
]


@pytest.mark.parametrize("inp,out", zip(INPUTS, OUTPUTS))
def test_all_cases(inp, out):
    assert parse_color(inp) == out
