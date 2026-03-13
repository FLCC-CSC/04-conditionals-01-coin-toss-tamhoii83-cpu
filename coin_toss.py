# FILE NAME - coin_toss.py

# NAME: Hoi I Tam
# DATE: March 12, 2026
# BRIEF DESCRIPTION:  This program generates a random number between 1 and 100 (inclusive).
# If the number is 51 or greater then Tails is reported. Otherwise Heads is reported.



########## ENTER YER CODE BELOW THIS LINE ##########

import random

print("===== Coin Flipper =====")
num = random.randint(1, 100)
if num >= 51:
    print("Tails")
else:
    print("Heads")



########### END YER CODE ABOVE THIS LINE ###########

'''

1. What was the hardest part of completing this lab? 
How to use the if statement to check the random number and print the result.

'''
