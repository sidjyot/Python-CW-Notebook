from turtle import *
n = int(input("Numbers to generate in Fibonacci Series? "))
a,b = 0,1
#print (a)
print (b)
pencolor('red')
circle(b*5)
penup()
for i in range(1,n):
  # if n == 1:
  #   print(a)
  #   print(b)
  # else:
    c = a + b
    print(c)
    a = b
    b = c
    pendown()
    pencolor('red')
    circle(c*5)
    penup()
    left(90)
    forward(c*5)


