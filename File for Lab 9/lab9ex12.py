def has23(List1:list) -> bool:
    """Returns True if the list contains a 2 or a 3 or both
    values. Otherwise, the function returns False .
    
    >>>has23([2,1,2,3,5,4])
    True
    >>>has23([2,1,3,5,4])
    True
    >>>?has23([2,1,1,1,1])
    False
    """
    for i in List1:
        if List1[i] == 2 or List1[i] == 3:
            return True 
        else:
            return False
    
List1 = [2,1,1,5,9]