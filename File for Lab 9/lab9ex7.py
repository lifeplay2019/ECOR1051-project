def reverse3(lst): 
    """
    Returns a new list containing the same
    elements in reverse order.
    
    >>>lst = [10, 11, 12] 
    [12, 11, 10]
    >>>lst = [11, 12, 13] 
    [13,12,11]
    """
    
    lst.reverse() 
    return lst 
      
lst = [10, 11, 12] 
print(reverse3(lst)) 