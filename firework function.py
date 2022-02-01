from turtle import *

def firework(colour1, colour2, x, y, length):
  pensize(4)
  penup()
  goto(x,y)
  pendown()
  for i in range(20):
    pencolor(colour1)
    forward(length)
    backward(length)
    right(9)
    pencolor(colour2)
    forward(length/2)
    backward(length/2)
    right(9)
  
# Test the function:
if __name__ == '__main__':
  bgcolor('black')
  firework('#fffb05', '#ff6e0d', -100, 60, 80)
  firework('#45d4ff', '#f520f5', -10, -70, 60)
  firework('#03ff3d', '#f51111', 110, 30, 50)