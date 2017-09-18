"""
Example 6-3: Recursive List
"""

x = None
for i in range(5, 0, -1):
    x = (i, x)

# wow, this looks gross :)
t1 = (1, 2)
t2 = (3, 4)
t = [t1, t2]
u = [t, t, t]
u[1] = u
t[0] = u
