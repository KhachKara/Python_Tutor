"""
Example 2-4
===========

Implementation of Selection Sort Algorithm
Author: Adnan Umer <u.adnan@outlook.com>
"""


def get_smallest(first, start):
    """
    Helper method ro find smallest number
    in list starting from specific index
    """
    # Let's Say number at start index is the smallest
    small = start
    for i in range(start + 1, len(first)):

        if first[i] < first[small]:
            # we found smaller number, update index
            small = i

    return small


def selection_sort(first):
    """
    Sorts list using Selection Sort Algorithm
    """

    # integrate len(lst) time
    for i in range(len(first)):

        # find smallest number ahead
        smallest = get_smallest(first, i)

        if smallest != i:
            # swap current element with smallest iff any
            first[smallest], first[i] = first[i], first[smallest]


# Sample unsorted list
lst = [38, 23, 15, 28, 59, 24, 40, 53]
print('Unsorted:', lst)

# call selection_sort for sample list
selection_sort(lst)
print('Sorted:', lst)
