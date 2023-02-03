# Cam Wysocki
# 10/4/22
# Lunch-o-matic

from pygame import QUIT


first_name= input('Please enter your first name. ')
print('Welcome, ' +first_name+ ', to the Lunch-O-Matic program.')
lunch= int(input('Please pick a number 1-5 to get your lunch recomendation. (Ex: 1) '))

if lunch == 1:
    print('You might find some joy in our pepperoni pizza, ' +first_name+ '!')
elif lunch == 2:
    print(first_name+ ',you seem to be the type who would love the chicken tenders!')
elif lunch == 3:
    print('Our spaghetti will do wonders for your taste buds, ' +first_name+ '!')
elif lunch == 4:
    print("So you're the one who likes the turducken; you've got fine tastes, " +first_name+ "!")
elif lunch == 5:
    print('Sushi it is, ' +first_name+ '!')
else:
    print('Glop, ' +first_name+ '. Just some glop. This is what you get for not following the rules, you monster.') 