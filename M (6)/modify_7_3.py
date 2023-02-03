# Cam W
# 10/10/22
# PRIMM Iteration Modify 7.3

number = int(input('Please enter a number: '))
counter = int(input('Please enter another number: '))
product= number*counter
while product < 1002:
  print(f'{number} * {counter} = {product}')
  product = product + 2
print('The loop has finished')