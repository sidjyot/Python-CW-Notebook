n = int(input('Please enter a number: '))

for i in range(2, n):
  if n % i == 0:
    print(n, ' is a Composite number')
    break
else:
  print(n, ' is a Prime number')