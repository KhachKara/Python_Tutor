"""
Example 3-1
===========

Finding Factorial with Recusion
Author: Adnan Umer <u.adnan@outlook.com>
"""

def fact(n):
    """
    Finds Factorial of given number using recusion
    """
    if n <= 1:  # factorial of 1 is 1
        return 1
    else:
        # factorial of n = n x [factorial of n -1]
        return n * fact(n - 1)

# find factorial of 6
fact6 = fact(6)
print('Factorial of 6 is', fact6)
