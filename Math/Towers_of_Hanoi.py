"""
Example 3-6
===========

Implementation of Towers of Hanoi algorithm to move
elements of one stack to another stack
"""


def TowerOfHanoi(fromStack, toStack, tempStack, toMove):
    """
    Moves stack of N elements from one stack to other 
    using temporary stack

    Parameters:
        toMove:     Number of elements in stack to move
        fromStack:  Stack from which to move elements
        toStack:    Stack to which to move elements
        tempStack: 	Empty temporary stack to use during moving
    """

    if toMove == 1:
        toStack.append(fromStack.pop())
    else:
        TowerOfHanoi(fromStack, tempStack, toStack, toMove - 1)
        toStack.append(fromStack.pop())
        TowerOfHanoi(tempStack, toStack, fromStack, toMove - 1)


fromStack = [4, 3, 2, 1]
toStack = []
tempStack = []

print("Before Moving", fromStack, '->', toStack)
# transfer 'fromStack' to 'toStack' using Tower of Hanoi rules
TowerOfHanoi(fromStack, toStack, tempStack, len(fromStack))

print("After Moving", fromStack, '->', toStack)
