

# Cam W
# 10/19/22
# Evidence Bank Balance

from random import randint
from time import sleep

# Use randint to get random number between -50 and 50 that is different every time unless you're 1% lucky.
# The rules state that it should be from 0 to 50 but it also says that in situation 1 it can be below 0.
# The title() function wasn't working, so deciding to skip that.

balance=randint(-50.00,50.00)

user=input('Welcome to our bank program. Please enter the name listed under your account. ')
# using the term "name listed under your account" because it feels more appropriate
sleep(3)
print(f'{user}, your balance is ${balance}.00.')
# Prints balance with necessary additives
sleep(2)
if balance<0:
    print(f'I\'m sorry, {user}, but your account has dropped below zero. You will be charged with a $35.00 penalty fee.')
elif balance==0:
    print(f'{user}, your account contains exactly $0; please consider adding funds soon.')
elif balance>0:
    print(f'{user}, your account is above $0 and doing well.')
input('Press ENTER to continue...')
# Talks to user directly, and does the "Press ENTER to continue" thing correctly.





