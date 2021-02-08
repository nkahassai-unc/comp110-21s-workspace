"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730411124"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint

# Begin your solution here...
numero = randint(1, 4)
print("Your fortune cookie says...")


if numero == 1:
        print("A dubious friend may be an enemy in camouflage.") 
else:
        if numero == 2:
            print("A cynic is only a frustrated optimist.")
        else:
            if numero == 3:
                print("No snowflake in an avalanche ever feels responsible")
            else:
                if numero == 4:
                    print("Your efforts have not gone unnoticed.")


print("Now, go spread positive vibes!")