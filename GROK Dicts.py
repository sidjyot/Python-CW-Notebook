#--------------------------------------------

phonebook = {}

line = input('Name and number: ')
while line:
  # parts = line.split()
  # name = parts[0]
  # number = parts[1]
  name, number = line.split()

  phonebook[name] = int(number)
  line = input('Name and number: ')

print(phonebook)

#--------------------------------------------

name_colour = {}

line = input('Name and colour: ')
while line:
  name, colour = line.split()
  name_colour[name] = str(colour)
  line = input('Name and colour: ')
  
#for i in name_colour:  
#  print(i, name_colour[i])

for k, v in name_colour.items():
  print (k, v)
  

#--------------------------------------------
car_colors = {}

input_color = input('Car: ')
while input_color:
  if input_color in car_colors:
    car_colors[input_color] += 1
  else:
    car_colors[input_color] = 1
  input_color = input('Car: ')
  
for k, v in car_colors.items():
  print(f'Cars that are {k}: {v}')
  
#--------------------------------------------
word_counter = {}

line = input('Enter line: ')
while line:
  words = line.split()
  for i in words:
    if i in word_counter:
      word_counter[i] += 1
    else:
      word_counter[i] = 1
  line = input('Enter line: ')
  
for k, v in sorted(word_counter.items()):
  print(f'{k} {v}')
  
#--------------------------------------------
