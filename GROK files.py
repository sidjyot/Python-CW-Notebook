#GROK files exercises
for line in open('orders.txt'):
  print(line.strip().upper())

#--------------------------------------
f = open('output.txt', 'w')
f.write("Hello, world!\n")
f.write("Now we're working with files!\n")
f.close()

#--------------------------------------
sounds = {'dog': 'a barker', 'cat': 'a meower', 'bird': 'a tweeter'}
f = open('output.txt', 'w')
for animal in sorted(sounds):
  sound = sounds[animal]
  print('A', animal, 'is', sound, sep='--', file=f)
f.close()

#--------------------------------------
#Using with to avaoid the f.close() part

sounds = {'dog': 'a barker', 'cat': 'a meower', 'bird': 'a tweeter'}

with open('output.txt', 'w') as f:
  for animal in sorted(sounds):
    sound = sounds[animal]
    print('A', animal, 'is', sound, sep='--', file=f)

#--------------------------------------
# letter.txt
My vegetable garden is growing really well!
WOOF! Let's play catch!
The tomatoes and cucumbers are nearly ready to eat.
How is your garden going?
WOOF! I better chase that possum!
#--------------------------------------
# fixed.txt
My vegetable garden is growing really well!
The tomatoes and cucumbers are nearly ready to eat.
How is your garden going?
#program.py
wf = open('fixed.txt', 'w')
for line in open('letter.txt'):
  if line[0:5] != 'WOOF!':
    print(line.strip(), file=wf)
wf.close()
#--------------------------------------
#book.txt
He looked out from the top of the mountain .
The colour of the sky was amazing .
Reds , oranges and pinks faded into a hazy blue.

#program.py
string1 = input('Word to look for: ').lower()

# opening a text file
file1 = open("book.txt", "r")

# setting flag and index to 0
flag = 0

# Loop through the file line by line
for line in file1:
	# checking string is present in line or not
  if string1 in line.lower():
    flag = 1
    break
# checking condition for string found or not
if flag == 0:
  print( string1 , 'was not found in the book.')
else:
  print( string1, 'was found in the book.')

# closing text file	
file1.close()

#--------------------------------------


