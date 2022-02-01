# c = input("Please enter a character: ")
# o = ord(c)

# print(f'The Unicode number of the character {c} is {o}')

# i = int(input("Please enter a Unicode number: "))
# c = chr(i)

# print(f'The printable character of the unicode {i} is {c}')

#Create a function that takes two arguments and returns thier product as a result

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

def product(first, second):
  c = first * second
  return c

d = product(a, b)
print(d)

