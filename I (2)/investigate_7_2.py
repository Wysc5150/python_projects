number = 7
print("I'm thinking of a number...Can you guess it?")
guess = int(input())
while guess != number:
  print("Incorrect! Guess again!")
  guess = (input())
  # It would help if this had int(input))
print("Correct! You got it!")

# Give the line number where iteration starts.
  # Answer: 4

# What does '!=' mean?
  # Answer: Is not equal to

# How many variables are there in the code?
  # Answer: 2

# How can you tell which lines of code are inside the loop?
  # Answer: White line behind them after while

# How many times will the loop repeat?
  # Answer: As many times as it takes to guess the number 7 (forever considering that int is not before input)

# What has to happen to make the script run the last line of code?
  # Answer: Input the correct answer