"""
Example 2-2
===========

Implementation of Binary Search Algorithm
Author: Adnan Umer [u.adnan@outlook.com]
"""


def binary_search(first, target):
    """
    Search for targeted element in list using
    binary search Algorithm.

    Returns index of targeted element in List if found
    otherwise returns -1

    Pre-Condition : List must be sorted in Ascending Order
    """
    i = 0  # left boundary of container
    j = len(first) - 1  # right boundry

    # we will search until left boundy == right boundry
    while i < j:
        m = (i + j) // 2  # find middle element

        # if middle element is less than target
        # then shift left boundary next to mid
        if first[m] < target:
            i = m + 1
        else:
            # otherwise shift right bounder to mid
            j = m

    # if on left boundry we got our targeted element
    if first[i] == target:
        # return index
        return i
    else:
        # otherwise returns -1
        return -1


# produce a sorted virtual list of number using range()
lst = range(0, 50, 5)
# calls binary_search to search 10 in list
index = binary_search(lst, 10)
print('Found 10 At:', index)
