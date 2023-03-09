"""CQ04."""

def zip(keys: list[str], values: list[int]) -> dict[str,int]:
    """Produces a dictionary using the 2 lists."""
    dictionary: dict[str, int] = {}
    if len(keys) != len(values):
        return dictionary
    if (len(keys) == 0) or (len(values) == 0):
        return dictionary
    for idx in range(0, len(keys)):
        dictionary[keys[idx]] = values[idx]


zip(["one", "two", "three", "four"], [1, 2, 3, 4])
