"""
Example 2-6
===========

Implementation of Merge Sort Algorithm
Author: Adnan Umer <u.adnan@outlook.com>
"""


def merge_sort(first):
    """
    Sorts list using merge sort Algorithm
    """
    n = len(first)
    if n <= 1:
        return first # single number is always sorted

    # split list into two parts from half
    left = first[:n / 2]
    right = first[n / 2:]

    # sort left and right parts
    leftSorted = merge_sort(left)
    rightSorted = merge_sort(right)

    # merge left and right sorted parts
    return merge(leftSorted, rightSorted)


def merge(left, right):
    """
    Merge two sorted lists in such a way resulting
    list is also sorted 
    """
    result = []

    # loop until left or right became empty
    while len(left) > 0 and len(right) > 0:

        # append smallest from both in result
        if left[0] < right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))

    # appends all the remaining items from
    # left and right
    result.extend(left)
    result.extend(right)

    return result

# Sample Unsorted list
first = [37, 50, 41, 31, 7, 32, 49, 78]
print('Unsorted:', first)

# call merge_sort for sample lst
merge_sort(first)
print('Sorted:', first)
