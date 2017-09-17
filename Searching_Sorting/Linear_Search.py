"""
Example 2-1:

Implementation of Linear Search Algorithm
Author: Adnan Umer [u.adnan@outlook.com]
"""


def linear_search(container, ele):
    """
	Uses linear search Algorithm to search container
	for specific element.

	Returns index of element in container if exits
	otherwise returns -1
	"""
    # to hanlde index with for loop
    # use range() function that returns virtual
    # list of number that will be used by for loop

    for i in range(len(container)):

        # checks wether element on current index
        # is required element of not
        if container[i] == ele:
            # if so returns index of element
            # REMEMBER: after encountering return statement
            # in function body, no more line is executed
            # So, searching operations stops after we found
            # our desired element
            return i

    # control comes here only when
    # Required element doesn't exists in container
    return -1


lst = [1, 2, 7, 3, 9, 2, 4, 6]  # Sample list
index = linear_search(lst, 7)  # call function to search 7 in lst
print('Found 7 at index', index)  # print index where we found 7
