"""
Example 3-5
===========

Demonstration of finding Greatest Common Divider (GCD)
"""


def gcd(a, b):
    """
    Calculates GCD of two given numbers
    """

    # Iterate until value of a becomes zero
    while a:
        # Assign remainder of b / a to a
        # and b becomes a.
        b, a = a, b % a

    # return value of b that is GCD
    return b


# Test for value 12.
res = gcd(6, 12)
print('GCD of 6 & 12 is', res)
