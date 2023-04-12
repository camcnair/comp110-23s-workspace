"""File to define River class."""
__author__ = "730408141"

from exercises.ex09.fish import Fish
from exercises.ex09.bear import Bear


class River:
    """River class."""

    day: int 
    bears: list[Bear]
    fish: list[Fish]

    def __init__(self, num_fish: int, num_bears:int):
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for x in range(0, num_fish):
            self.fish.append(Fish())
        for x in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        """Checks ages of fish and bears and removes old ones."""
        surviving_fish: list[Fish] = self.fish.copy()
        surviving_bears: list[Bear] = self.bears.copy()
        for fish in self.fish:
            if fish.age > 3:
                surviving_fish.remove(fish)
        for bear in self.bears:
            if bear.age > 5:
                surviving_bears.remove(bear)
        self.fish = surviving_fish
        self.bears = surviving_bears
        return None

    def bears_eating(self):
        """Allows bears to eat fish and removes fish from the river."""
        for bear in self.bears:
            if len(self.fish) >= 5:
                bear.eat(3)
                self.remove_fish(3)
        return None
    
    def check_hunger(self):
        """Checks the hunger of each bear and removes bears with a hunger score of 0."""
        new_bear_list: list[Bear] = []
        for bear in self.bears:
            if bear.hunger_score > 0:
                new_bear_list.append(bear)
        self.bears = new_bear_list
        return None
        
    def repopulate_fish(self):
        """Reproduces fish."""
        fish_count: int = len(self.fish)
        for idx in range(fish_count // 2):
            self.fish.append(Fish())
            self.fish.append(Fish())
            self.fish.append(Fish())
            self.fish.append(Fish())
        return None
    
    def repopulate_bears(self):
        """Repopulates bears."""
        bear_count: int = len(self.bears)
        for idx in range(bear_count // 2):
            self.bears.append(Bear())
        return None
    
    def view_river(self):
        """Prints day, fish number, and bear number."""
        x = self.day
        y = len(self.fish)
        z = len(self.bears)
        print(f"~~~ Day {x}: ~~~")
        print(f"Fish population: {y}")
        print(f"Bear population: {z}")
        return None
    
    def one_river_day(self):
        """Simulate one day of life in the river."""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def one_river_week(self):
        """Simulates one week in the river."""
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        return None
    
    def remove_fish(self, amount: int):
        """Removes an amount of fish from the river."""
        for idx in range(amount):
            self.fish.pop(idx)
        return None