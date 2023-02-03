# Predict & Run 7.1

# Example 1
# Add comments to each line to say whehter it is inside or outside the loop and what the code does
# Explain what must happen for the loop to run

print("What is the capital of France?\n")
answer = input() 

while answer != "Paris":
    print("Sorry, incorrect! Try again!")
    answer = input("What is the capital of France?")

print("Correct!")
# The iteration will start if your input does not match the condition, and the loop will end once your input matches the condition

# Example 2
counter = 1

while counter < 5:
    print("This line of code is inside the loop.")
    counter += 1
# The iteration will make the counter will increase by 1 until it is greater than or equal to the condition(5)