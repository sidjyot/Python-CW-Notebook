#reverse words in a string
text = input('Please enter a sentence to reverse: ')
word = ''
rev_string = ''
#str_end = text[-1]

for i in text:
  word = f'{word}{i}'
  #if (i == ' ' or s == str_end):
    rev_string = word + rev_string 
    print(rev_string)
    word = ''
  