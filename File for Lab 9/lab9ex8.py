def max_end3(lst):
    """Return the value of the max_ends as the value that lst[0] and lst[2] which
    is bigger
    In the statement that I have provided have two kind condition.
    
    Example:
    
    max_end3(lst1)
    [1,1,1]
    max_end3(lst2)
    [2, 2, 2]    
    """
    if lst[0]>lst[2]:
        return [lst[0],lst[0],lst[0]]
    if lst[0]<lst[2]:
        return [lst[2],lst[2],lst[2]]
    else:
        return False
    
    
lst1=[1,10,0]
lst2=[1,10,2]