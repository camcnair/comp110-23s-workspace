"""EX07: Dictionary Functions."""
__author__ = "730408141"


def invert(input_dict: dict[str, str]) -> dict[str, str]:
    """Inverts the keys and values of a given dict."""
    new_dict: dict[str, str] = {}
    for key in input_dict:
        value: str = input_dict[key]
        if value in new_dict:
            raise ValueError("There cannot be more than one of the same key.")
        new_dict[value] = key
    return new_dict


def favorite_color(input_dict: dict[str, str]) -> str:
    """Returns the color that appears most often in a dictionary."""
    favorite_color: str = ""
    counts: dict[str, int] = {}
    highest_count: int = 0
    for key in input_dict:
        color: str = input_dict[key]
        if color in counts:  # adds 1 more for the count of that color
            counts[color] += 1
        else:  # color has not already been counted
            counts[color] = 1
        if counts[color] > highest_count:  # establishes the color with the new highest count
            favorite_color = color
            highest_count = counts[color]    
    return favorite_color


def count(input_list: list[str]) -> dict[str, int]:
    """Counts the number of times a value appears in a given list."""
    counts: dict[str, int] = {}
    for item in input_list:
        if item in counts:  # item already exists in counts
            counts[item] += 1
        else:  # item doesn't exist in counts already, value is established 
            counts[item] = 1
    return counts