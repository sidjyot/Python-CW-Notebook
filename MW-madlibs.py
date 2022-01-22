'''
name1 = input('Enter a name: ')
name2 = input('Enter another name: ')
planet = input('Enter a planet: ')
thing = input('Enter a thing: ')
vehicle = input('Enter a vehicle: ')
verb = input('Enter a verb ending in ing: ')
animal = input('Enter an animal: ')
adjective = input('Enter an adjective: ')
place = input('Enter a place: ')

#print('Hello ' + name + '!')
output_string = name1 + " and " + name2 + " went to " + planet + " in search of " + thing + ". They travelled on their " + vehicle + ". Once they reached, they started " + verb + " everywhere. Suddenly they were stopped by a " + animal + ". It was so " + adjective + " that they decided to bring it back to " + place

print(output_string)
'''

# Using F-string
#name = input('Please enter your name: ')
#print(f'Hello {name}!')

my_list = []
print('Please enter values for name, another name, a planet & a thing, one value per line')
print('Enter "done" (without the quotes) to end')

while True:
  s = input('value: ')
  if s == 'done':
    break
  my_list.append(s)

output_string = my_list[0] + " and " + my_list[1] + " went to " + my_list[2] + " in search of " + my_list[3] + "."

print(output_string)

# #Simple addition calculation
# first = input('Please enter first number: ')
# second = input('Please enter second number: ')
# sum = int(first) + int(second)
# print(f'The sum of {first} and {second} is {sum}')
