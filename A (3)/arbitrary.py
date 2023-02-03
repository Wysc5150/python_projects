# Cam W
# 11/7/22
# Sandwiches

def sandwich(*innards):
    #print(f'One order of a(n) {innards} sandwich')
    print('Adding the following ingredients to your sandwich:')
    for innard in innards:
        print(f'- {innard}')

sandwich('american cheese', 'bolagna', 'mayo', 'ham', 'pickles', 'lettuce', 'bacon')

sandwich('mayo', 'cheddar cheese')

sandwich('ranch')




def fav_char(*character):
    print(f'My favorite character in gaming is {character[0]} and my favorite in comics is {character[1]}.')

fav_char('Goro Akechi', 'Batman')