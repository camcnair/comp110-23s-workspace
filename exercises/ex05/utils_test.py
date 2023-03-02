"""Unit Tests for EX05."""
__author__ = "730408141"

from exercises.ex05.utils import only_evens

def test_empty_only_evens() -> None:  # edge case
    """Tests only_evens with an empty list."""
    test_list: list[int] = []
    assert only_evens(test_list) == []


def test_only_odds() -> None:  # use case
    """Tests only_evens with a list of only odd numbers."""
    test_list: list[int] = [1, 3, 5, 7, 9]
    assert only_evens(test_list) == []


def test_many() -> None:  # use case
    """Tests only_evens with multiple numbers in the list."""
    test_list: list[int] = [1, 2, 3, 4, 5, 6, 7, 8]
    assert only_evens(test_list) == [2, 4, 6, 8]


def test_negatives() -> None:  # use case
    """Tests only_evens with negative numbers."""
    test_list: list[int] = [-1, -2, -3, -4, -5, -6]
    assert only_evens(test_list) == [-2, -4, -6]


from exercises.ex05.utils import concat

def test_empty() -> None:  # edge case
    """Tests concat with an empty list"""
    test_list1: list[int] = []
    test_list2: list[int] = []
    assert concat(test_list1, test_list2) == ['[][]']


def test_many_concat() -> None:  # use case
    """Tests concat with multiple items in each list."""
    test_list1: list[int] = [1, 2, 3, 4, 5]
    test_list2: list[int] = [6, 7, 8, 9, 10]
    assert concat(test_list1, test_list2) == ['[1, 2, 3, 4, 5][6, 7, 8, 9, 10]']


def test_with_different_lengths() -> None:  # use case
    """Tests concat with 2 lists of different lengths."""
    test_list1: list[int] = [1, 2, 3, 4, 5, 6]
    test_list2: list[int] = [7, 8]
    assert concat(test_list1, test_list2) == ['[1, 2, 3, 4, 5, 6][7, 8]']


from exercises.ex05.utils import sub

def test_empty_sub() -> None:  # edge case
    """Tests sub with an empty list."""
    test_list: list[int] = []
    start: int = 0
    stop: int = 2
    assert sub(test_list, start, stop) == []


def test_negative_start() -> None:  # edge case
    """Tests sub with a negative start value."""
    test_list: list[int] = [1, 2, 3, 4, 5]
    start: int = -2
    stop: int = 4
    assert sub(test_list, start, stop) == [1, 2, 3, 4]


def test_start_too_large() -> None:  # edge case
    """Tests sub with a start value that is larger than the length of the list."""
    test_list: list[int] = [1, 2, 3, 4, 5]
    start: int = 7
    stop: int = 8
    assert sub(test_list, start, stop) == []


def test_typical_sub() -> None:  # use case
    """Tests sub with typical use."""
    test_list: list[int] = [1, 2, 3, 4, 5, 6, 7]
    start: int = 2
    stop: int = 5
    assert sub(test_list, start, stop) == [3, 4, 5]


def test_typical_sub_negatives() -> None:  # use case
    """Tests sub with typical use and negative numbers in the list."""
    test_list: list[int] = [-1, -2, 0, -4, -5]
    start: int = 0
    stop: int = 4
    assert sub(test_list, start, stop) == [-1, -2, 0, -4]