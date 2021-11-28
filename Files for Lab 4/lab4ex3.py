# the header of the function
def accumulated_amount(principal, rate, n, time):
   return principal * (1+rate/n)**(n*time)
# get the value that you want
# the function get to 0 when the principal is the value of 0
# if the interests is 0 the value that you get is still 1500
# Yes my function does the correct value when wnter the test case
