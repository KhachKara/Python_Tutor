"""
Examples 5-4: Link List using Class
"""

class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next

y = None
for i in range(6, 0, -1):
    y = Node(i, y)
