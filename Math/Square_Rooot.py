"""
Example 3-4
===========

Calculating square roots by Newton's method, inspired by SICP
http://mitpress.mit.edu/sicp/full-text/book/book-Z-H-10.html#%_sec_1.1.7

According to this method we start guessing square root from 1
and checks validity of guess. If guess was not correct we improves
our guess i.e new guess is always equals to average of last guess and
number divided by last guess. This continues untill we reached
to approx figure that is square root of number
"""


def sqrt(x):
    """
    Calculates square root of X using Newton's method
    """

    def average(a, b):
        # Returns average of two numbers
        return (a + b) / 2.0

    def is_good_enough(guess):
        # Returns true if guess is near to real square root
        return abs((guess * guess) - x) < 0.001

    def improve(guess):
        # Improves the guess and teturns new guess
        return average(guess, x / guess)

    def sqrt_iter(guess):
        # Function that will be recursively called
        # until we found square root
        if is_good_enough(guess):
            return guess
        else:
            return sqrt_iter(improve(guess))

    # Starts the square root guess iteration from 1
    return sqrt_iter(1.0)

# Call method to find square root of 9
# Excepted is 3 but we will got a values
# approx equals 3
ans = sqrt(9)