# Cam Wysocki
# 03 OCT 2022
# Trivia Quiz

score = 0
number_of_questions = 3

# Get user's first name
first_name = input("Please enter your first name- ")
# Add custom welcome message that includes the user's first name
print("Hello, " + first_name + ", and welcome to my trivia quiz. There will be 3 questions in this quiz.")

# Build questions and checking the user's answers
print("Question 1")
print('Which is the hardest enemy in Final Fantasy VII? ')
print('a. Emerald Weapon')
print('b. Chocobo')
print('c. Sephiroth')
print('d. Ruby Weapon')
answer1 = input("Answer: ")

# Use an IF/ELSE statement to check user's answer against the correct answer
if answer1 == 'd':
    # Tell user they got it right
    print('Correct!')
    # Update the user's score
    score = score + 1
else:
    # Tell user they got the question wrong
    print('Incorrect!')

print("Question 2")
print("Which character is known for hunting ghosts and being in his brother's shadow? ")
print('a. Link')
print('b. Cloud')
print('c. Luigi')
print('d. Samuel Joseph Wurzelbacher')
answer2 = input("Answer: ")

# Use an IF/ELSE statement to check user's answer against the correct answer
if answer2 == 'c':
    # Tell user they got it right
    print('Correct!')
    # Update the user's score
    score = score + 1
else:
    # Tell user they got the question wrong
    print('Incorrect!')

print("Question 3")
print("Which character is known for partnering up with Disney characters and weilding the Keyblade? ")
print('a. Sora')
print('b. L-Tetrimino')
print('c. Snake')
print('d. Ted Lasso')
answer3 = input("Answer: ")
# Use an IF/ELSE statement to check user's answer against the correct answer
if answer3 == 'a':
    # Tell user they got it right
    print('Correct!')
    # Update the user's score
    score = score + 1
else:
    # Tell user they got the question wrong
    print('Incorrect!')

# Do the math
final_score = (score / number_of_questions) * 100
print("Thank you for playing my trivia quiz, " + first_name + ", your final score was " + str(score) + ", which is " + str(final_score) Cam+ ".")