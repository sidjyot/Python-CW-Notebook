#Robots in a Line
line = input('Line: ')
upper_line = line.upper()
words = line.split()
upper_words = upper_line.split()

if 'robot' in words:
  print('There is a small robot in the line.')
elif 'ROBOT' in words:
  print('There is a big robot in the line.')
elif 'ROBOT' in upper_words:
  print('There is a medium sized robot in the line.')
else:
  print('No robots here.')
  
#Line: There's a strobotron at the concert.
#Line: Look at the rOBOt down the road.
#Line: I'm baking chocolate robot brownies.
#
