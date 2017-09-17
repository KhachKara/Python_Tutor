"""
Example 1-4:
============

Filtering Python Lists
"""

sample_list = [ 25, 'Huzaifah', 38, 'Adnan' , 54, 'Mani' ]

def filter_marks(lst):
    """
    Filters integers from list and returns a tuple
    having first element list of integers
    and second element is rest of list
    """
    integers = []
    rest = []

    for ele in lst: # interate over list

        # 'type' will returns type of element
        # if type of element is integer append
        # element to integers list
        if type(ele) is int:
            integers.append(ele)
        else:
            # otherwise append in rest list
            rest.append(ele)

    # multiple comma seprated values are returned
    # as tuple in python
    return integers, rest

# tuple result from function can be unpacked
# directly by placing equal number of comma seprated
# variables on left side
integers, rests = filter_marks(sample_list)

print('Integers: ', ', '.join([str(x) for x in integers]))  # join list with defined seprater
print('Others: ', ', '.join(rests))  # join list with defined seprater
