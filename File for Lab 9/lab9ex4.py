def common_end(L1: list, L2: list)-> bool:
    """Returns True if they have the same first element or the same last element 
    or if the first and last elements of both lists are the same. Otherwise, 
    the function returns False .
    
    Example:
    common_end(test_list1,test_list2)
    Faluse
    
    
    """
    
    if L1[0]==L2[0] or L1[-1]==L2[-1]:
        return True
    if L1[0]==L1[-1] or L2[0]==L2[-1]:
        return True
    else:
        return False
    
test_list1 = [0, 1, 2, 3, 4, 5]
test_list2 = [6, 1, 2, 3, 4, 9]    
test_list3 = [6, 1, 2, 3, 4, 6]