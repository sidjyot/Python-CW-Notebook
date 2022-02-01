# Translate the emoji
def emoji_translate(emoji_code):
  if 128511 < emoji_code < 128519:
    return ':-)'
  elif 128543 < emoji_code < 128546:
    return '>:-('
  elif emoji_code == 128546:
    return ":'‑("
  elif 128538 < emoji_code < 128542:
    return ':‑P'
  else:
    return "Sorry, I don't know that emoji!"

# Add your code after this.
emoji = input('Emoji? ')
emoji_code = ord(emoji)
translated_emoji = emoji_translate(emoji_code)
print(translated_emoji)

