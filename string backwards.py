def backwards(text):
  backwards_text = ''
  for c in text:
    backwards_text = f'{c}{backwards_text}'
    #print(c, backwards_text)
  return backwards_text

print(backwards('How the hell'))