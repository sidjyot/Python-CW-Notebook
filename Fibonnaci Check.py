n = int(input("Number to check in Fibonacci Series? "))
f_2,f_1 = 1,1
f = f_2 + f_1
while f < n: 
  if n == 1:
    print(f'{n} is a Fibonacci number!')
    break
  else:
    f = f_2 + f_1
    if f == n:
      result =  'is a Fibonacci number!'
      break
    result = 'is NOT a Fibonacci number!'
    f_2 = f_1
    f_1 = f
print(f'{n} {result}')

