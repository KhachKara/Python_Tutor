"""
Example 5-2: Immutable Link List
"""

y = None
for i in range(6, 0, -1):
    y = (i, y)