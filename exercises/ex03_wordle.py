"""Exercise 03: Wordle"""
__author__ = "730408141"

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
user_guess: str = ""

def contains_char(word: str, character:str) -> bool:
    """Searches through the first string to determine if the character is present."""
    assert len(character) == 1
    word_index: int = 0
    while word_index < len(word):
        if word[word_index] == character:
            return True 
        else:  # character is not present at current index
            word_index = word_index + 1
    return False  # character is not present in word

def emojified(guess: str, secret: str) -> str:
    """Returns color coded emojis if letters in the 2 strings match."""
    assert len(guess) == len(secret)
    guess_index: int = 0
    emoji_str: str = ""
    while guess_index < len(secret):
        if guess[guess_index] == secret[guess_index]:
            emoji_str = emoji_str + GREEN_BOX
        else:  # letter at current index of guess does not match letter at current index of secret 
            if contains_char(secret, guess[guess_index]) is True:
                emoji_str = emoji_str + YELLOW_BOX
            else:  # letter is not found anywhere in secret word
                emoji_str = emoji_str + WHITE_BOX
        guess_index = guess_index + 1
    return emoji_str 

def input_guess(ex_length: int) -> str:
    """Prompts user for a guess of expected length and returns user's guess"""
    global user_guess
    user_guess = input(f"Enter a {ex_length} character word: ")
    while len(user_guess) != ex_length:
        user_guess = input(f"That wasn't {ex_length} chars! Try again: ")
    return user_guess

def main() -> None:
    """The entrypoint of the program and main game loop"""
    SECRET_WORD: str = "codes"
    turns: int = 1
    playing: bool = True
    global user_guess
    while (turns <= 6) and playing is True:
        print(f"=== Turn {turns}/6 ===")
        print(emojified(input_guess(5), SECRET_WORD))
        if user_guess == SECRET_WORD:
            playing = False
            print(f"You won in {turns}/6 turns! ")
        else:  # input guess did not match the secret word
            turns = turns + 1
    if turns > 6:
        print("X/6 - Sorry, try again tomorrow! ")

if __name__ == "__main__":
    main()