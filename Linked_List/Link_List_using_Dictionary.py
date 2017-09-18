"""
Example 5-3: Link List using Dictionary
"""

# use dicts
x = None
for i in range(6, 0, -1):
    x = {'data': i, 'next': x}
