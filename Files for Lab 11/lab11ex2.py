def divisors(n):
    """Return the value of the resukt set the result
    
    # Testing the function here. ignore/remove the code below if not required
    print(divisors(6))
    print(divisors(9))
    
    
    
    >>>divisors(9)
    [1, 3, 9]
    >>>divisors(6)
    [1, 2, 3, 6]
    """
    result = []
    for i in range(1, n + 1):
        if n % i == 0:
            result.append(i)
    return result