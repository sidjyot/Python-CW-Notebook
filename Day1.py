#Print a string
print("Hello World!")

#print using single quotes
print('Hello World!')

#Creating a variable
message = 'Hello World!'
print(message)

#Creating a variable
message = 'Hello World!'
message2 = 'Hello Earth!'
message = message2
print(message)

# Taking input
#name = input('Please enter your name: ')
#print('Hello ' + name + '!')

# Using F-string
#name = input('Please enter your name: ')
#print(f'Hello {name}!')

# #Simple addition calculation
# first = input('Please enter first number: ')
# second = input('Please enter second number: ')
# sum = int(first) + int(second)
# print(f'The sum of {first} and {second} is {sum}')

name = input("Please enter your name: ")
gender = input("Please enter your gender (M/F): ")

if(gender == 'M'):
  print(f'Hello Mr. {name}')

if(gender == 'F'):
  print(f'Hello Ms. {name}')
