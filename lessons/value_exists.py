"""Value Exists Function."""


def value_exists(x: dict[str, int], y: int) -> bool:
    """Returns True if the int exists in the dictionary, and False otherwise."""
    for key in x:
        if x[key] == y:
            return True
    return False