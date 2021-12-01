#Part A - the solution from 1 to 5
#" and' for the str but in the type is the same
#>>> type('Hello')
#is <class 'str'>
# With "" the solution will be '' , however with the ' in the "" then the solution will be "'"
#* , / , // and - valid operators when both operands are strings
# It doesn't matter that if left-hand or right-hand operand of *
#+ , - , / , and // valid operators when one operand is a string 
#It doesn't matther if it is the right hand or the left hand side.
#the string '123' is not as same as the integer 123 
#
#
#




#Part B - exercise 6
def repeat(s: str, n: int) -> str:
    """ Return s repeated n times; if n is negative, return the
    empty string.
    >>> repeat('yes', 4)
    'yesyesyesyes'
    >>> repeat('no', 0)
    >>> repeat('no', -2)
    >>> repeat('yesnomaybe', 3)
    """
    if (n > 0):
        return s * n
    """Return the value with the condition with n>=0 get the solution with s*n
    s  str
    n  int
    
    condition n >= 0
    """
    if (n <= 0):
        return ""
    """Return the value with the condition with n>=0 get the solution with ""
    s  str
    n  int
    
    condition n <= 0
    """  