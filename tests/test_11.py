from collections import OrderedDict

import pytest

from python_hw_1 import dict_merge, product, transpose, uniq


TRANSPOSE_TEST_CASES = OrderedDict(
    [
        ("transpose_test_case_0", ([[1, 2], [3, 4], [5, 6]], [[1, 3, 5], [2, 4, 6]])),
        ("transpose_test_case_1", ([[1, 2], [3, 4]], [[1, 3], [2, 4]])),
        ("transpose_test_case_2", ([[1], [3]], [[1, 3]])),
        ("transpose_test_case_3", ([[1, 3]], [[1], [3]])),
        ("transpose_test_case_4", ([[1]], [[1]])),
    ]
)


@pytest.mark.parametrize(
    "matrix,expected",
    TRANSPOSE_TEST_CASES.values(),
    ids=list(TRANSPOSE_TEST_CASES.keys()),
)
def test_transpose(matrix, expected):
    assert transpose(matrix) == expected


UNIQ_TEST_CASES = OrderedDict(
    [
        ("uniq_test_case_0", ([1, 2, 3, 3, 1, 7], [1, 2, 3, 7])),
        ("uniq_test_case_1", ([1, 1, 3, 1, 1, 3], [1, 3])),
        ("uniq_test_case_2", ([1], [1])),
        ("uniq_test_case_3", ([], [])),
    ]
)


@pytest.mark.parametrize(
    "sequence,expected", UNIQ_TEST_CASES.values(), ids=list(UNIQ_TEST_CASES.keys())
)
def test_uniq(sequence, expected):
    assert list(uniq(sequence)) == expected


DICT_MERGE_TEST_CASES = OrderedDict(
    [
        (
            "dict_merge_test_case_0",
            ([{1: 2}, {2: 2}, {1: 1}], {1: 1, 2: 2}),
        ),
        ("dict_merge_test_case_1", ([{1: 2}, {1: 3}, {1: 1}], {1: 1})),
        ("dict_merge_test_case_2", ([{1: 2}, {2: 3}, {3: 4}], {1: 2, 2: 3, 3: 4})),
        ("dict_merge_test_case_3", ([{}, {}, {3: 4}], {3: 4})),
    ]
)


@pytest.mark.parametrize(
    "dicts,expected",
    DICT_MERGE_TEST_CASES.values(),
    ids=list(DICT_MERGE_TEST_CASES.keys()),
)
def test_dict_merge(dicts, expected):
    assert dict_merge(*dicts) == expected


PRODUCT_TEST_CASES = OrderedDict(
    [
        ("product_test_case_0", ([1, 2, 3], [4, 5, 6], 32)),
        ("product_test_case_1", ([1, 2], [3, 4], 11)),
        ("product_test_case_2", ([1], [1], 1)),
    ]
)


@pytest.mark.parametrize(
    "lhs,rhs,expected", PRODUCT_TEST_CASES.values(), ids=list(PRODUCT_TEST_CASES.keys())
)
def test_product(lhs, rhs, expected):
    assert product(lhs, rhs) == expected
