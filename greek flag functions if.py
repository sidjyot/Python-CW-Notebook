from turtle import *
FLAG_LEN = 270
FLAG_WID = 180

length = FLAG_LEN
breadth = int(FLAG_WID/9)
flag_color1 = '#0d5eaf'
flag_color2 = 'white'
# Define the draw_line function here:
def fill_rect(length, breadth, colour):
  bgcolor('white')
  fillcolor(colour)
  begin_fill()
  pendown()
  forward(length)
  right(90)
  forward(breadth)
  right(90)
  forward(length)
  right(90)
  forward(breadth)
  right(90)
  penup()
  end_fill()
    
if __name__ == "__main__":
  for i in range(9):
    if (i % 2) == 0: 
      colour = flag_color1
    else:
      colour = flag_color2
    fill_rect(length,breadth, colour)
    left(90)
    forward(breadth)
    right(90)
    
  penup()
  right(90)
  forward(breadth)
  left(90)
  colour = flag_color1
  fill_rect(5*breadth, 5*breadth, colour)
  colour = flag_color2
  forward(2*breadth)
  fill_rect(breadth,5*breadth,colour)
  backward(2*breadth)
  right(90)
  forward(2*breadth)
  left(90)
  fill_rect(5*breadth,breadth,colour)
  