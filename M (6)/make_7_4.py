# Cam Wysocki
# 10/10/22
# PRIMM Make 7.4 Activity

from time import sleep


password='abc123'

username=input('Please enter your username: ')
sleep(1)
userpswrd=input('Please enter your password: ')
sleep(1)

while userpswrd!=password:
    print('Incorrect password, please try again.')
    sleep(1)
    userpswrd=input()
print(f'Access granted; welcome, {username}.')
