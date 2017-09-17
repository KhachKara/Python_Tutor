"""
Example 2-3
===========

Implementation of Bubble Sort Algorithm
Author: Adnan Umer <u.adnan@outlook.com>
"""


def bubble_sort(first):
    """	
	Sorts the list in ascending order using bubble sort algorithm.
	"""
    # iterate len(lst) times
    for i in range(len(first)):

        # integrate [len(lst) - i - 1] times
        for j in range(len(first) - i - 1):

            # sort two number if not sorted
            if first[j] > first[j + 1]:
                # swap element at j with element at j + 1
                # and element ad j + 1 with element j
                first[j], first[j + 1] = first[j + 1], first[j]


# unsorted list of numbers
first = [6, 8, 42, 8, 35, 8, 9, 12]
print('Unsorted:', first)

# call bubble_sort for lst
bubble_sort(first)
print('Sorted:', first)
