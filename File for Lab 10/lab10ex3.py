def has22(list_one:list)->bool:
    """Returns True if the list contains a 2 next to a
    2. Otherwise, the function returns False .
    
    
    >>>has22([1,2,2,3])
    True
    >>>has22([1,2,3,4])
    False
    
    
    """
    if ', 2, 2' in str(list_one):
        return True
    elif list_one[0] == 2 and list_one[1] == 2:
        return True
    else:
        return False