# Replace the exclamation marks with question marks.
def questionify(text):
  # Complete this function! Write your code below:
  new_text = ''
  for c in text:
    if c == '!':
      c = '?'
    new_text = f'{new_text}{c}'
  return new_text 
  
if __name__ == '__main__':
  # You can use this to test your function.
  # Any code inside this if statement will be ignored by the automarker.
  
  # Test the first example in the question.
  print(questionify('How did you do that!'))
  
  # Test the second example in the question.
  print(questionify('Oh no!!! Why!'))

  # You can add more tests here!
  