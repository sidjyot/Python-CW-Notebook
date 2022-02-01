#patterns with numbers
n = int(input('Please enter a number: '))

def leading_number(number):
  for i in range(1, number+1):
    for j in range(i):
      print(i,end='')
    print('\n',end='')

#leading_number(n)

def trailing_number(number):
  space = ' ' * (number-1)
  for i in range(1, number+1):
    for j in range(i):
      if j == 0:
        print(f'{space}{i}',end='')
      else:    
        print(f'{i}',end='')
    print('\n',end='')
    number -= 1
    space = ' ' * (number-1)

#trailing_number(n)

def pyramid(number):
  space = ' ' * (number-1)
  for i in range(1, number+1):
    for j in range(2*i-1):
      if j == 0:
        print(f'{space}{i}',end='')
      else:    
        print(f'{i}',end='')
    print('\n',end='')
    number -= 1
    space = ' ' * (number-1)

#pyramid(n)    

def desc_number(number):
   for i in range(1, number):
    for j in range(i):
      print(f'{i-j} ',end='')
    print('\n',end='')

desc_number(n)

