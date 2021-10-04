"""Unit tests for list utility functions."""

# TODO: Uncomment the below line when ready to write unit tests
from exercises.ex05.utils import only_evens, sub, concat

__author__ = "730224009"


# testing only_evens
def test_only_evens_none() -> None:
    assert only_evens([3, 5, 7]) == []


def test_only_evens_empty() -> None:
    assert only_evens([]) == []


def test_only_evens_full() -> None:
    assert only_evens([1, 2, 3, 4, 5, 6]) == [2, 4, 6]


# testing sub
def test_sub_neg_start() -> None:
    assert sub([1, 2, 3], -3, 1) == [1]


def test_sub_normal() -> None:
    assert sub([3, 9, 6, 12], 1, 3) == [9, 6]


def test_sub_small_end() -> None:
    assert sub([0, 3, 8, 13, 44], 2, -3) == []


# testing concat
def test_concat_normal() -> None:
    assert concat([1, 2, 3], [4, 5, 6]) == [1, 2, 3, 4, 5, 6]


def test_concat_uno_empty() -> None:
    assert concat([], [12, 33, 19]) == [12, 33, 19]


def test_concat_both_empty() -> None:
    assert concat([], []) == []


