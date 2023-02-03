# Cam W
# 10/25/22
# Calculator

print('Enter two numbers')
num1=0
num2=0

def add(num1, num2):
    answer=num1+num2
    return answer

def subtract(num1, num2):
    answer=num1-num2
    return answer

def multiply(num1, num2):
    answer=num1*num2
    return answer

def divide(num1, num2):
    answer=num1/num2
    return answer

def power(num1, num2):
    answer=num1**num2
    return answer

print('Would you like to add(1), subtract(2), multiply(3), divide(4), or raise to the power of(5)?')
choice=input('')

if choice!='5':
    print('Now please choose 2 numbers')
elif choice=='5':
    print('Now please choose a number and the power you would like to raise it to')
num1=int(input())
num2=int(input())

if choice=='1':
    print(f'The answer is {add(num1, num2)}')
elif choice=='2':
    print(f'The answer is {subtract(num1, num2)}')
elif choice=='3':
    print(f'The answer is {multiply(num1, num2)}')
elif choice=='4':
    print(f'The answer is {divide(num1, num2)}')
elif choice=='5':
    print(f'The answer is {power(num1, num2)}')

