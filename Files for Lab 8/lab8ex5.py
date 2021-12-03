def sum_uniques (a:int, b:int, c:int) -> int:
    """return the sum of the value of all unique int:
    
    """
    if a == b and b==c and a==c:
        return 0
    elif a == b or b==c or a==c:
        if a==b:
            return c
        if a==c:
            return b
        if b==c:
            return a
    else:
        return a+b+c