"""
Example 1-5
===========

Tokenizing string to extract specific informations
from string.

Requisite: String pattern must be known
"""

# input string with known pattern
# String Pattern:
#       First Name
#       Last Name
#       Year of Birth
#       Month of Birth
#       Day of Birth
#       Gender

input_ = 'Adnan,Umer,1995,8,17,male'

# split input string on seprater
# in this case seprater is ','
tokens = input_.split(',')

firstName = tokens[0]
lastName = tokens[1]

# int(str) to convert string to integer
birthdate = (int(tokens[2]), int(tokens[3]), int(tokens[4]))
isMale = (tokens[5] == 'male')

print('Howday!', firstName, lastName)
