def search4vowels(phrase:str) -> set:
    """ВОзвращает гласные, найденые в фразе."""
    vowels = set('aeiou')
    return vowels.intersection(set(phrase))


def search4letters(phrase: str, letters: str = 'aeiou') -> set:
    """Возвращает множество букв из 'letters', найденых в указаной фразе."""
    return phrase, set(letters).intersection(set(phrase))
