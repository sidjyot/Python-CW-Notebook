from turtle import *

def draw_flag():
  pendown()
  pensize(1)
  pencolor('black')
  for i in range(2):
    forward(200)
    right(90)
    forward(160)
    right(90)
  penup()


def draw_horizontal_rectangle():
  pendown()
  pensize(1)
  pencolor('white')
  for i in range(2):
    forward(100)
    right(90)
    forward(30)
    right(90)
  penup()

def draw_vertical_rectangle():
  pendown()
  pensize(1)
  pencolor('white')
  for i in range(2):
    forward(30)
    right(90)
    forward(100)
    right(90)
  penup()

penup()
goto(-200,80)
fillcolor('#FF0000')
begin_fill()
draw_flag()
end_fill()

goto(-150,15)
fillcolor('#FFFFFF')
begin_fill()
draw_horizontal_rectangle()
end_fill()

goto(-115,50)
fillcolor('#FFFFFF')
begin_fill()
draw_vertical_rectangle()
end_fill()

