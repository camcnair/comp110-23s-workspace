"""File to define Fish class."""


class Fish:
    """Fish class."""

    age: int

    def __init__(self):
        """Initializes the fish's attribute."""
        self.age = 0
        return None
    
    def one_day(self):
        """Increases fish's age by 1 day."""
        self.age += 1
        return None