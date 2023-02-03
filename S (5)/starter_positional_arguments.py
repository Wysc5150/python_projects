# Cam W
# 10/31/22
# Starter Positional Arguments

# Positional arguments example
def describe_pet(pet_name, animal_type):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type }'s name is {pet_name.title()}.")
    
# A dog named Rover
describe_pet('rover', 'dog')

# A hamster named Harrison
describe_pet('harrison', 'hamster')

# Call the describe_pet ( ) function a third time, similar
# to what you see on line 12 above

# Use 'marko' and 'dog' as your two arguments, but switch the order
# of the arguments so that 'dog' is the first argument and 'marko' is
# the second argument
describe_pet('dog', 'marko')

# How does changing the order of your arguments affect your output?
# (Write your answer here) It make sit so I have a marko named Dog

# Next, define a function that uses two positional arguments, 
# first name and programming language, to display an output string
# that summarizes which programming language the person is trying to learn

# For example: Mackenzie is trying to learn Python.

# Call the function twice, and use different names and programming languages each time
# Tell Python to capitalize the person's name and the programming language correctly in
# the output (even if the user enters the first name and language in lowercase)

def programming(first_name, program):
    """Display person and the program they are trying to learn"""
    print(f'\n {first_name.title()} is trying to learn {program.title()}.')

programming('koren', 'Python')

programming('Skylar', 'java')