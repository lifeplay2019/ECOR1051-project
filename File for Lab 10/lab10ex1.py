def count_evens(List1:list) -> int:
    """The function takes a list of integers, which may be empty. The
    function returns the number of even integers in the list.
    
    
    >>>count_evens([1,2,3,4])
    [2,4]
    >>>count_evens([2,4,6,8])
    [2,4,6,8]
    """
    enum = []
    for n in List1:
        if n % 2 == 0:
                enum.append(n)
        return enum
        