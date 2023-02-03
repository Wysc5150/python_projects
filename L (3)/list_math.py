from turtle import update


names=['Skylar', 'Koren', 'Clayton', 'Danny', 'Jacob']
temps=[40, 42, 43, 44, 45]

print(names.index('Koren'))
print(temps.index(45))

del names[0]
names.insert(0, 'Biggs')
print(names)

print(min(temps), max(temps), sum(temps))

titles=['Spiderman: Into the Spider-verse', 'The Eye of Minds', 'Lord of the Flies', 'The Nightmare Before Christmas', 'Red Notice']

for title in titles:
    print(title)

# #7 answer: Yes; the number will be greater for the more number of items in your list.

# #8 answer: You can use the len() function

# #9 answer: The first index number will always be 0

numbers1=[15, 79, 839, 92, 1]
numbers2=[45, 6, 7431, 309, -3]

for index in range(len(numbers1)):
    print(f'{numbers1[index]} times {numbers2[index]} equals {numbers1[index] * numbers2[index]}.')

