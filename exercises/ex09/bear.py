"""File to define Bear class"""

class Bear:
    
    # attributes:
    age: int
    hunger_score: int 


    def __init__(self): 
        """Initializes the bear's attributes."""
        self.age = 0
        self.hunger_score = 0
        return None
    

    def one_day(self):
        """Increases bear's age by 1 day and decreases hunger score by 1."""
        self.age += 1
        self.hunger_score -= 1
        return None
    

    def eat(self, num_fish: int):
        """Allows bear to eat a certain number of fish."""
        self.hunger_score += num_fish
        return None