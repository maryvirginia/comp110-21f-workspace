"""Unit tests for dictionary functions."""

# TODO: Uncomment the below line when ready to write unit tests
from exercises.ex06.dictionaries import invert, favorite_color, count

__author__ = "730224009"


def test_invert_short() -> None:
    """Ensures invert returns inversion of short given dict."""
    assert invert({"m": "a", "r": "y"}) == {"a": "m", "y": "r"}


def test_invert_long() -> None:
    """Ensures invert returns inversion of long given dict."""
    assert invert({"v": "i", "r": "g", "i": "n", "a": "a"}) == {"i": "v", "g": "r", "n": "i", "a": "a"}


def test_invert_empty() -> None:
    """Ensures invert return empty dict when given empty dict."""
    assert invert({}) == {}


def test_favorite_color_three() -> None:
    """Ensures favorite_color returns most frequent color."""
    assert favorite_color({"MV": "blue", "Joey": "blue", "Gigi": "purple"}) == "blue"


def test_favorite_color_four() -> None:
    """Ensures favorite_color returns empty str when given empty dict."""
    assert favorite_color({"G": "blue", "T": "blue", "H": "blue", "D": "white"}) == "blue"
    

def test_favorite_color_tie() -> None:
    """Ensures favorite_color returns first most popular color when there is a tie."""
    assert favorite_color({"Tinker Bell": "green", "Tiana": "green", "Cinderella": "blue", "Moana": "blue"}) == "green"


def test_count_unique_keys() -> None:
    """Ensures count establishes dict of frequencies when given list with unique str."""
    assert count(["MV", "Joey", "Gigi"]) == {"MV": 1, "Joey": 1, "Gigi": 1}


def test_count_same_keys() -> None:
    """Ensures count returns dict of frequencies when given list with same str."""
    assert count(["Niall", "Niall", "Harry", "Louis", "Niall", "Liam", "Niall", "Zayn", "Harry"]) == {"Niall": 4, "Harry": 2, "Louis": 1, "Liam": 1, "Zayn": 1}


def test_count_empty() -> None:
    """Ensures count returns empty dict when given empty list."""
    assert count([]) == {}