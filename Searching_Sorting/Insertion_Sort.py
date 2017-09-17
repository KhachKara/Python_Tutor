"""
Example 2-5
===========

Implementation of Insertion Sort Algorithm
Author: Adnan Umer <u.adnan@outlook.com>
"""


def insertion_sort(first):
    """
    Sorts list using Insertion Sort Algorithm
    """

    # iterate for [length of list] times
    for i in range(len(first)):
        j = i

        # keep shift number to left until we got
        # smaller number on left or we reached
        # on start of list
        while j > 0 and first[j] < first[j - 1]:
            first[j], first[j - 1] = first[j - 1], first[j]  # swaps
            j -= 1  # moves left


# Sample Unsorted list
lst = [25, 15, 46, 40, 17, 69, 79, 69, 82, 29]
print('Unsorted:', lst)

# call insertion_sort for sample list
insertion_sort(lst)
print('Sorted:', lst)
