# Cam W
# 10/31/22
# Starter Keyword Arguments

# Keyword arguments example
def describe_person(first_name, last_name, hair_color):
    '''A simple function that describes a person.'''
    print(f'{first_name.title()} {last_name.title()} has {hair_color} hair.')

# Using keyword arguments in the function call
describe_person(first_name='mike', last_name='reardon', hair_color='blond')
describe_person(first_name='elizabeth', last_name='carlson', hair_color='light brown')

# Write a function that summarizes:
# what city a person was born in
# what city that person lives in now


# For example:
# Michaela was born in Houston, but now lives in Seattle.
def city(first_name, home, current):
    print(f'\n{first_name.title()} grew up in {home.title()}, and currently lives in {current.title()}')

# Use three keyword arguments in your function call and update
# the docstring for your new function
# Call the function twice and use different names and cities for each function call
# Make sure Python correctly capitalizes the names and cities (even if the user enters the names
# and cities in lowercase)
city(first_name='Danny', home='kingsley', current='Detroit')
city(first_name='manton', home='Clayton', current='fife lake')

# In the first function call, the order of your keyword arguments should match the order of the
# parameters in your parameter list

# In the second function call, the order of your keyword arguments should NOT match the order of
# the parameters in your parameter list

# Remember to enclose your docstring for your function in a pair of triple quotation marks