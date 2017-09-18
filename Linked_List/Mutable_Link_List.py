"""
Example 5-1: Mutable Link List
"""

x = None
for i in range(6, 0, -1):
    x = [i, x]

y = None
for i in range(9, 3, -1):
    y = [i, y]

x[1][0] = y[1][1]
