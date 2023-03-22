"""Odd and Even."""


def odd_and_even(x: list[int]) -> list[int]:
    """Returns a new list containing the elements of the input list that are odd and have an even index."""
    new_list: list[int] = []
    for idx in range(0, len(x)):
        if (x[idx] % 2 != 0) and (idx % 2 == 0):
            new_list.append(x[idx])
    return new_list
