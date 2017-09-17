"""
Example 3-2
===========

Prints Fibonacci series using python list
"""

arr = [1, 1]
print(arr[0])
i = 0
# Sky is the limit
while True:
    # prints last element of series
    print(arr[-1])

    # take sum of current elements in array
    tmp = sum(arr)
    # append sum in array
    arr.append(tmp)
    # and delete first element
    del arr[0]
    i += 1
    if i == 100:
        break