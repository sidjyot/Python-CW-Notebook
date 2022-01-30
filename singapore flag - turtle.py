from turtle import *

def draw_rectangle():
  pendown()
  pensize(1)
  pencolor('black')
  for i in range(2):
    forward(200)
    right(90)
    forward(75)
    right(90)
  penup()

def draw_circle():
  pendown()
  circle(25)
  penup()

def draw_star():
  pendown()
  pencolor('#FFFFFF')
  for i in range(5):
    forward(10)
    right(144)
  penup()
  

penup()
goto(-200,100)
fillcolor('#FF0000')
begin_fill()
draw_rectangle()
end_fill()

right(90)
forward(75)
left(90)
draw_rectangle()

penup()
pencolor('#FFFFFF')
left(90)
forward(12)
right(90)
forward(50)
fillcolor('#FFFFFF')
begin_fill()
draw_circle()
end_fill()

penup()
forward(10)
pencolor('#FF0000')
fillcolor('#FF0000')
begin_fill()
draw_circle()
end_fill()

penup()
forward(18)
left(90)
forward(40)
right(90)
for star in range(5):
  draw_star()
  right(72)
  forward(18)

hideturtle()


