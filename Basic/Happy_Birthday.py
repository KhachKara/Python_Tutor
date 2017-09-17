"""
Example 1-2
===========
Says Happy Birthday to me [Adnan Umer]
using functions
"""


def say_happy_birthday():
    """
    Prints "Happy Birthday to you!" in console
    """
print("Happy Birthday to you!")


def sing(person_name):
    """
    Sings Happy Birthday song for given person name
    """
    say_happy_birthday()
    say_happy_birthday()
    print("Happy Birthday dear " + person_name + "!")
    say_happy_birthday()

sing("Adnan Umer")
