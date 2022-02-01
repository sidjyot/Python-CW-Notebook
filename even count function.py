# Count how many letters have an even Unicode value.
def even_count(word):
  count = 0
  for letter in word:
    unicode_num = str(ord(letter))
    if unicode_num[-1] in '24680':
      count = count + 1
  return count

# Add your code after this.
name = input('Give me a name: ')
ec1 = even_count(name)
ec2 = even_count('Steven')
if ec1 == ec2:
  print('Even Steven!')
else:
  print('That name is not as even as Steven.')
  
