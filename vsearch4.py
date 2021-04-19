def search4letters(phrase: str, letters: str= 'aeuio') -> set:
    """Returns the set of 'letters' found in 'phrase'."""
    return set(letters).intersection(set(phrase))