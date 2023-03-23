"""Tests for EX07."""
__author__ = "730408141"


from exercises.ex07.dictionary import invert
from exercises.ex07.dictionary import favorite_color
from exercises.ex07.dictionary import count 


def test_invert_long() -> None:  # use case
    """Tests the invert function when the dictionary is very long."""
    test_dict: dict[str, str] = {'courtney': 'mcnair', 'caroline': 'kelly', 'katie': 'hubbard', 'emily':'russell', 'sophie': 'moghadam', 'alexa': 'monroe', 'alex': 'hutchins', 'cameron': 'harris'}
    assert invert(test_dict) == {'mcnair': 'courtney', 'kelly': 'caroline', 'hubbard': 'katie', 'russell': 'emily', 'moghadam': 'sophie', 'monroe': 'alexa', 'hutchins': 'alex', 'harris': 'cameron'}


def test_invert_normal() -> None:  # use case
    """Tests the invert function for normal use with a dictionary."""
    test_dict: dict[str, str] = {'color': 'blue', 'food': 'italian', 'music': 'rock'}
    assert invert(test_dict) == {'blue': 'color', 'italian': 'food', 'rock': 'music'}


def test_invert_empty() -> None:  # edge case
    """Tests the invert function with an empty dictionary."""
    test_dict: dict[str, str] = []
    assert invert(test_dict) == {}


def test_fav_color_2() -> None:  # use case
    """Tests favorite_color function when there are 2 colors tied for highest count."""
    test_dict: dict[str, str] = {'Mike': 'orange', 'Chrissy': 'blue', 'Kelly': 'orange', 'Jared': 'blue'}
    assert favorite_color(test_dict) == 'orange'


def test_fav_color_norm() -> None:  # use case
    """Tests favorite_color function with normal use and only 1 color with highest count."""
    test_dict: dict[str, str] = {'Courtney': 'blue', 'Sophie': 'purple', 'Michelle': 'blue', 'Chris': 'green'}
    assert favorite_color(test_dict) == 'blue'


def test_fav_color_empty() -> None:  # edge case
    """Tests favorite_color function with an empty dict."""
    test_dict: dict[str, str] = {}
    assert favorite_color(test_dict) == ''


def test_count_normal() -> None:  # use case
    """Tests the count function with normal use and input list."""
    test_list: list[str] = ["hello", "hey", "hello", "howdy"]
    assert count(test_list) == {"hello": 2, "hey": 1, "howdy": 1}


def test_count_single() -> None:  # use case
    """Tests the count function with a single item in the input list."""
    test_list: list[str] = ["courtney"]
    assert count(test_list) == {"courtney": 1}


def test_count_empty() -> None:  # edge case
    """Tests the count function with an empty input list."""
    test_list: list[str] = []
    assert count(test_list) == {}