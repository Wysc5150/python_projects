import time

print('Name 3 friends in order of friendship (good-not as good)')
time.sleep(3)
friend1=input('')
time.sleep(1)
friend2=input('')
time.sleep(1)
friend3=input('')
time.sleep(3)
friend2_2=friend2

friends=[]

friends.append(friend1)
friends.append(friend2)
friends.append(friend3)

print(f'Your friends are {friends}')
time.sleep(2)

friend4=input('You made a new friend who is nicer than friend 2, who is it? ')
time.sleep(2)

friends.insert(1, friend4)

print(f'Your friendship list is now {friends}')

print('Now let\'s say one of your friends did something unforgivable, and you had to break the bond.')
time.sleep(4)
unfriend=input('Would you like it to be (in the order you input them 1-4, not the order they are currently in) friend 1, 2, 3, or 4? ex(3) ')
time.sleep(6)

if unfriend=='1':
    friends.remove(friend1)

elif unfriend=='2':
    friends.remove(friend2)

elif unfriend=='3':
    friends.remove(friend3)

elif unfriend=='4':
    friends.remove(friend4)

time.sleep(2)
print(f'Your friendship list is now {friends}')
time.sleep(2)

print('Suddenly, your close friend drifts away and your least close friend is supporting you.')
time.sleep(5)

friends.reverse()

print(f'Your friendship list is now {friends}')
time.sleep(4)

print('You happen to make another friend that shares the name as one of your (ex)friends')
time.sleep(5)

friends.append(friend2)

print(f'You now have {friends.count(friend2_2)} friend(s) named {friend2}, and your friendship list is now {friends}.')
time.sleep(6)

print('Unfortunately that new friend was actually getting revenge for the friend you let go. So obviously you let them go too.')
time.sleep(6)

friends.pop(3)

print(f'Your final friendship list is {friends}. Thank you for Participating.')