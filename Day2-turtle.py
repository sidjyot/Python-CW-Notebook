from turtle import *

def draw_rectangle():
  pendown()
  pensize(1)
  pencolor('black')
  for i in range(2):
    forward(200)
    right(90)
    forward(50)
    right(90)
  penup()

def draw_wheel():
  pendown()
  pencolor('#000080')
  circle(25)

  left(90)
  forward(25)

  for i in range(24):
    forward(25)
    backward(25)
    left(360/24)
    
  penup()

penup()
goto(-200,100)
fillcolor('#FF9933')
begin_fill()
draw_rectangle()
end_fill()
right(90)
forward(50)
left(90)

draw_rectangle()
right(90)
forward(50)
left(90)

fillcolor('#138808')
begin_fill()
draw_rectangle()
end_fill()

forward(100)
draw_wheel()
