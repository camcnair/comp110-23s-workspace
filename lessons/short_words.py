"""Short Words."""


def short_words(x: list[str]) -> list[str]:
    """Returns list of words that are shorter than 5 characters."""
    new_list: list[str] = []
    for word in x:
        if len(word) < 5:
            new_list.append(word)
        else:
            print(f"{word} is too long.")
    return new_list