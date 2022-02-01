from turtle import *

bgcolor('skyblue')
fillcolor('royalblue')

pensize(7)
pencolor('mediumblue')

num_sides = int(input('How many sides? '))
turn_angle = 360/num_sides

begin_fill()
for i in range(num_sides):
  forward(45)
  left(turn_angle)
end_fill()