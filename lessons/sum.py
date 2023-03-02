"""Example Function for Unit Tests."""

def sum(xs: list[float]) -> float:
    """return sum of all elements in xs"""
    sum_total: float = 0.0
    for items in xs:
        sum_total += items
    return sum_total