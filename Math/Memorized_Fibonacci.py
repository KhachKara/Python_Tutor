"""
Example 3-3
===========

Demonstration of memorized Fibonacci series implementation
"""

# Dictionary to save computed results
memoTable = { }


def memoizedFibonacci(n):

    # First two elements of Fibonacci series are `1`
    if n <= 2: return 1

    # Don't re-compute value if its already calculated
    if n in memoTable:
        # returns the computed value
        return memoTable[n]

    # Calculates values of Fibonacci series element
    # at N place using f(n) = f(n - 1) + f(n - 2)
    # i.e In Fibonacci each items if series is sum of
    # previous two elements
    memoTable[n] = memoizedFibonacci(n - 1) + \
                    memoizedFibonacci(n - 2)

    # Returns the saved values from table
    return memoTable[n]

# Test function. Expected value of 10 is 55
print(memoizedFibonacci(10))