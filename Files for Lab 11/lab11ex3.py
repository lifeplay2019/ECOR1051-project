def reverse(lst):
    """Returns a new list that contains all the elements of the original
    list in reverse order.
    
    # create a new list with size same as the input parameter lst
    # iterate n(length of list) times
    # set item i of lst in reversed position of result
    
    
    >>>reverse([4, 2, 3, 2])
    [2, 3, 2, 4]

    >>>reverse([2, 3, 2, 4])
    [4, 2, 3, 2]
    """
    result = [0] * len(lst)  
    for i in range(len(lst)):  
        result[len(lst) - i - 1] = lst[i]  
    return result  