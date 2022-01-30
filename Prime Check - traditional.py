n = int(input('Please enter a number: '))


flag = 'prime'


for i in range(2, n):
  if n % i == 0:
    flag = 'composite'
    break
  
if flag == 'prime':
  print(n, ' is a prime number')
else:
  print(n, ' is a composite number')