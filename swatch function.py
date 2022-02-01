from turtle import *

# Draws one swatch
def draw_swatch(x, y, colour):
  # Complete the function to draw a swatch:
  penup()
  goto(x,y)
  pendown()
  pensize(2)
  fillcolor(colour)
  begin_fill()
  for i in range(4):
    forward(30)
    left(90)
  end_fill()
  

# Draw the grid
draw_swatch(-60, 50, 'yellow')
# Add more swatches here:
draw_swatch(-15, 50, 'gold')
draw_swatch(30, 50, 'lightsalmon')
draw_swatch(-60, 0, 'DarkSeaGreen2')
draw_swatch(-15, 0, 'PaleGreen3')
draw_swatch(30, 0, 'plum')
draw_swatch(-60, -50, 'skyblue')
draw_swatch(-15, -50, 'cornflowerblue')
draw_swatch(30, -50, 'orchid3')


