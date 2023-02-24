"""Exercise 04: Utils"""
__author__ = "730408141"

def all(x: list[int], y: int) -> bool:
    """Indicates whether the int is the same as all ints in the list"""
    list_idx: int = 0
    while list_idx < len(x):
        if y != x[list_idx]:
            return False
        list_idx += 1
    return True

def max(input: list[int]) -> int:
    """Returns the largest number in a list"""
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    input_idx: int = 0
    max: int = 0
    while input_idx < len(input):
        if input[input_idx] > input[input_idx + 1]:
            max = input[input_idx + 1]
        input_idx += 1
    return max

def is_equal(list1: list[int], list2: list[int]) -> bool:
    """Indicates whether 2 lists are equal to each other"""
    idx: int = 0
    if len(list1) != len(list2):
        return False
    while (idx < len(list1)) and (idx < len(list2)):
        if list1[idx] != list2[idx]:
            return False
        idx += 1
    return True