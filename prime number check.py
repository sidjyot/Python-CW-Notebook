# Check if the number is a Prime number
prime = int(input("Enter a positive integer to check whether it's a prime number: ")) 
num_fact = 1

for i in range(1,prime):
  if prime % i == 0:
    num_fact += 1
  #else:
   # x = 0
if num_fact == 2:
  print(f'{prime} is a Prime number!')
else:
  print(f'{prime} is a Composite number! with {num_fact} factors')
  















# ---------------------------------------------------
# def iseven(prime):
#   if prime % 2 == 0:
#     print(f' The {prime} is even')
#     num_fact = 10
#   else:
#     print(f' The {prime} is odd')


# def isprime(prime):
#   if num_fact == 2:
#     print('{prime} is a Prime number!')
#   else:
#     print('{prime} is a Composite number!')

# iseven(prime)
# isprime(prime)