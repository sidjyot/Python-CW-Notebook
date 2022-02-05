phonebook = {}

line = input('Name and number: ')
while line:
  parts = line.split()
  name = parts[0]
  number = parts[1]
  phonebook[name] = int(number)
  line = input('Name and number: ')

print(phonebook)