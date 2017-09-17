"""
Example 1-3
===========

Introduces Python Programming Language to novices
"""


# Python Numbers
age = 26        # Integer
pi = 3.14159    # Floating point number

# Python Strings
string = 'Adnan Umer'
tokens = string.split()  # splits string on space and return parts

# List Indexing [Indexing Starts from Zero]
firstName = tokens[0]       # get first element of list
lastName = tokens[1]        # get second element of list

# String Concatenation
my_name = firstName + ' ' + lastName

# 'if' statement
if string == my_name:  # : at the end of lines means block of code ahead
    # Indentation matters in Python
    # Blocks is defined by indenting all lines of
    # blocks with equal spaces or tabs on left
    print('Yes! Both strings are same')
else:
    print('No! Both strings are not same')

# Python List [Mutable Sequence]
students = ['Adnan', 'Zain', 'Aown']
students.append('Ali')  # inserting another item in list

# 'for' loop
# integrates over collections
for student in students:
    # Indentation matters alot

    # all arguments seprated by comma in front of 'print'
    # are joined placing a space between them and printed
    # on console
    print('Hello!', student)

# Python Tuple [Immutable Sequence]
ages = (19, 22, 18)

# Python Set [No order, No duplicates]
uniqueAges = set(ages)
uniqueAges.add(18)      # already in set, no effect
uniqueAges.remove(22)   # removing from set

# no guaranteed order when iterating over a set
for thisAge in uniqueAges:
    print(thisAge)

# testing set membership
if 18 in uniqueAges:
    print('There is an 18-year-old present!')

# sorting
students.sort() # in-place
orderedUniqueAges = sorted(uniqueAges) # sorting results in new list

# Python Dictionary - Mapping unique keys to values
netWorth = { }
netWorth['Donald Trump'] = 3000000000
netWorth['Bill Gates'] = 58000000000
netWorth['Tom Cruise'] = 40000000
netWorth['Joe Postdoc'] = 20000

# iterating over key-value pairs:
for (person, worth) in netWorth.items():
    if worth < 1000000:
        print('Hmm!', person, 'is not a millionaire')

# testing dictionary membership
if 'Tom Cruise' in netWorth:
    print('show me the money!')
