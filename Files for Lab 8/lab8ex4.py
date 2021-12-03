def blackjack(a:int, b:int) -> int:
    """ return the value closest to 21 while still being under 21 if both value 
    are over to 21 , the return the value to 0
    
    >>> def blackjack(17,22)
    17
    >>>def blackjack(23,24)
    0
    >>>def blackjack(17,19)
    19
    
    """
    
    if a > 21 and b > 21 :
        return 0
    elif a > 21:
        return b
    elif b > 21:
        return a
    elif (a-b) > 0:
        return a
    else:
        return b
        
  
    
                
                
                
