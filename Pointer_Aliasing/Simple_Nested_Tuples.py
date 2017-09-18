"""
Example 6-1: Nested Tuples
"""

# Simple
a = (1, (2, (3, None)))
b = a[1]

c = (1, (2, None))
d = (1, c)

# Complex
l1, l2, l3, l4 = 1, 2, 3, 4

t1 = (l1, l2)
t2 = (l3, l4)
t = (t1, t2)
u = ((1, 2), (3, 4))
v = u[0]
