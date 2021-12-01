#Exercise 8


def replicate(character: str) -> str:
    """Return the replicate of character
    character is a string
    
    len--length of the character
    >>> replicate("acde")
    'acdeacdeacdeacde'
    >>>replicate("character")
    'charactercharactercharactercharactercharactercharactercharactercharactercharacter'
    >>>replicate("rbq")
    'rbqrbqrbq'
    
    """
    return character * len(character)

replicate("rbq")
replicate("acde")
replicate("character")