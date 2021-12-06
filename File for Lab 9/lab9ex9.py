def sum2(numList):
    """Return the value of sum2 with 2 condition one of it is the value of 
    empty list which return to 0
    Another return the sum of the lis[0]+lis[2]
    
    
    >>>sum2([1,2,3,4,5])
    3
    >>>sum2([])
    0

    """
    if list(numList) == []:
        return 0
    else:
        return numlist[0]+numlist[1]

numlist = [1,2,3,5,6]