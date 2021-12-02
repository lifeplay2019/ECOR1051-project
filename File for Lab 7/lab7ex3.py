import math

def factorial(n: int) -> int:
    """ Return n! for postive values of n.
    
    >>> factorial(1)
    1
    >>> factorial(2)
    2
    >>> factorial(3)
    6
    >>> factorial(4)
    24
    """
    fact = 1
    for i in range(2, n+1):
        fact=fact*n
    return fact

testpass = 0
testfail = 0
for j in range(1, 5):
    expected = math.factorial(j)
    actual = factorial (j)
    if expected == actual:
        print ("Expected Result: ", expected, " Actual Result: ", actual, "\n Test Passed", sep='')
        testpass += 1
    else:
        print ("Expected Result: ", expected, " Actual Result: ", actual, "\r Test Failed", sep='')
        testfail += 1
print(testpass, " tests passed \r", testfail, " tests failed\r", sep='')