from turtle import *

# Define your dandelion function here:
def dandelion(x,y,length):
  penup()
  goto(x,-150)
  pendown()
  pensize(3)
  pencolor('#91F485')
  goto(x,y)
  angle = 360/40
  for i in range(20):
    pencolor('#0085C7')
    forward(length)
    backward(length)
    left(angle)
    pencolor('#009F3D')
    forward(length)
    backward(length)
    left(angle)
    
if __name__ == "__main__":
  # Test your function
  bgcolor('#ECFAF5')
  dandelion(-0, 50, 60)
  
  # Add your own tests here:
  dandelion(-100, 40, 60)
  dandelion(-50, -50, 30) 