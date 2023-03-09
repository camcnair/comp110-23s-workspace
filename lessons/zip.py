"""CQ04."""
__author__ = "730408141"


def zip(keys: list[str], values: list[int]) -> dict[str,int]:
    """Produces a dictionary using the 2 lists."""
    dictionary: dict[str, int] = {}
    if len(keys) != len(values):
        return dictionary
    if (len(keys) == 0) or (len(values) == 0):
        return dictionary
    for idx in range(0, len(keys)):
        dictionary[keys[idx]] = values[idx]