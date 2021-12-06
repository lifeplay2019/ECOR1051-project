def make_ends(List1:list) -> list:
    """Return the valuea new list of containing the first and last elements
    from the original list.
    
    
    >>>List1 = [1,2,3,4,5,6]
    [1,6]
    >>>List1 = [1,2,3,4,5,7]
    [1,7]
    """
    return  [List1[0], List1[-1]]

List1 = [1,2,3,4,5,6]