"""Exercise 05: List Utily Functions."""
__author__ = "730408141"

def only_evens(xs: list[int]) -> list[int]:
    """Returns only the even integers in a given list."""
    evens: list[int] = []
    for idx in range(0, len(xs)):
        if xs[idx] % 2 == 0:  # determines if value is even
            evens.append(xs[idx])
    return evens 


def concat(list1: list[int], list2: list[int]) -> list[str]:
    """Concatenates 2 lists of ints into 1 list."""
    combined_list: list[int] = list1 + list2
    return combined_list


def sub(a_list: list[int], start: int, stop: int) -> list[int]:
    """Generates a subset of a given list."""
    modified: list[int] = []
    if start < 0:  # negative start value
        start = 0
    if stop > len(a_list):  # stop value too large
        stop = len(a_list)
    if (a_list == 0) or (start >= len(a_list)) or (stop <= 0):  # empty list, too large of a start value, too small of a stop value
        modified = []
        return modified 
    for idx in range(start, stop):
        modified.append(a_list[idx])
    return modified



