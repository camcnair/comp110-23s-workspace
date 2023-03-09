"""Choose your own adventure."""
__author__ = "730408141"


import random


points: int = 0
player: str = ""
playing: bool = True
death_time: int = random.randint(1, 5)
QUESTIONING: str = "\U0001F9D0" 
MONEY_BAG: str = "\U0001F4B0"
MAGNIFY: str = "\U0001F50E"


def main() -> None:
    """Main game loop."""
    global points
    points = 0
    global playing
    greet()
    while playing is True:
        print(f"{MAGNIFY} Your current adventure points: {points}")
        path: str = input(f"{MAGNIFY} Would you like to investigate the library (A), the study (B), the ballroom (C), or try to earn bonus adventure points (D)? Or, would you prefer to stop playing (E)? Answer with the capital letter associated with that option: ")
        if path == "A":  # chose to investigate the library 
            A()
        if path == "B":  # chose to investigate the study 
            B()
        if path == "C":  # chose to investigate the ballroom
            C()
        if path == "D":  # chose to try for bonus points
            points = D(points) 
        if path == "E":  # chose to stop playing
            print(f"{MAGNIFY} Come back soon, {player}! Your total adventure points: {points}")
            playing = False


def greet() -> None:
    """Greets the player."""
    global player 
    player = input(f"{MAGNIFY} Welcome brave adventurer! What is your name? ")
    print(f"{MAGNIFY} Welcome {player}! You have been tasked with solving the murder of Colonel Mustard within the Mustard estate. The murder occurred during a dinner party hosted by Colonel Mustard, in which his guests, and prime suspects, include Mrs. Peacock, Ms. Scarlet, and Mr. Green. The body was found in the entryway, and the murder weapon is reported to be a revolver based on the gunshot wounds inspected on his body. The police are holding each suspect in different rooms until you can solve the case and ensure that the murderer is captured. Police on the scene reported that whoever is the murderer would surely have the murder weapon on them still, since they arrived to the scene only {death_time} minutes after they received the call. Each choice you make will earn you a certain number of \"adventure points\" to be totaled at the end of the game. It is up to you to catch this killer and solve the murder of Colonel Mustard before the killer strikes again!")


def A() -> None:
    """Investigates the library."""
    global points
    global playing
    investigate: str = ""
    print(f"{MAGNIFY} You enter the library to find Mrs. Peacock.")
    investigate = input(f"{MAGNIFY} {player}, Would you like to question Mrs. Peacock {QUESTIONING}? Answer with Yes or No. ")
    if investigate == "Yes":
        print(f"{MAGNIFY} You question Mrs. Peacock and this is her response: \"I am telling you the truth. I did not murder Colonel Mustard. He has been a dear friend of mine for as long as I can remember and I am absolutely devastated at these tragic events.\"")
        points += 1
    else:  # chose not to investigate
        points += -1
    print(f"{MAGNIFY} After searching her possessions as well as the room, you do not find the murder weapon, however you do find a dagger. While it is concerning that Mrs. Peacock has a dagger, she is not the murderer. You must continue your search of the other suspects and rooms. ")
    points += 2  # points increased for investigating this room


def B() -> None:
    """Investigates the study."""
    global points
    global playing
    investigate: str = ""
    print(f"{MAGNIFY} You enter the study to find Mr. Green.")
    investigate = input(f"{MAGNIFY} {player},Would you like to question Mr. Green {QUESTIONING}? Answer with Yes or No. ")
    if investigate == "Yes":
        print(f"{MAGNIFY} You question Mr. Green and this is his response: \"Are you fools going to let us go anytime soon? I am telling you that I had nothing to do with the horrible thing that happened to Colonel Mustard. Best to keep on your search, because you are going to get nowhere with me.\"")
        points += 1
    else:  # chose not to investigate
        points += -1
    print(f"{MAGNIFY} After searching his possessions as well as the room, you do not find the murder weapon, however you do find rope. While it is concerning that Mr. Green has rope, he is not the murderer. You must continue your search of the other suspects and rooms.")
    points += 2  # points increased for investigating this room


def C() -> None:
    """Investigates the ballroom."""
    global points
    global playing
    investigate: str = ""
    print(f"{MAGNIFY} You enter the ballroom to find Ms. Scarlet.")
    investigate = input(f"{MAGNIFY} {player},Would you like to question Ms. Scarlet {QUESTIONING}? Answer with Yes or No. ")
    if investigate == "Yes":
        print(f"{MAGNIFY} You question Ms. Scarlet and this is her response: \"Alright. You caught me. But Colonel Mustard had it coming. Trust me, I was doing everyone a favor. He has taken money from his friends, including me, on more than one occasion. I did what I had to do and ensured that it would never happen again.\"")
        points += 1
    else:  # chose not to investigate
        points += -1
    print(f"{MAGNIFY} After searching her possessions as well as the room, you find the murder weapon: the revolver she used to kill Colonel Mustard. You alert the police that the murder weapon was in her possession and they swiftly arrest her. You, as well as the other guests, go home triumphantly knowing that the killer was caught.")
    points += 2  # points increased for investigating this room
    print(f"{MAGNIFY} Your final adventure points: {points}")
    playing = False


def D(x: int) -> int:
    """Opportunity for player to earn bonus points."""
    stolen: int = random.randint(2000, 4000)
    print(f"{MAGNIFY} Hello, {player}, while you have been searching the rooms and suspects, police have continued investigating and found that a signifant sum of money, between $2000 and $4000 {MONEY_BAG}, has gone missing from Colonel Mustards bank account. Therefore, they concluded that the motive of the killer was surely to acquire this money. If you can correctly guess the amount of money withdrawn within $500, you will earn 5 bonus adventure points.")
    guess: int = int(input(f"{MAGNIFY} How much money do you think was stolen? Answer without a dollar sign. "))
    if (stolen - guess > 500) or (guess - stolen > 500):
        print(f"{MAGNIFY} Sorry, that wasn't close enough.")
        return x
    else:  # guess was close enough to value
        print(f"{MAGNIFY} You got it, {player}!")
        x += 5
        return x


if __name__ == "__main__":
    main() 