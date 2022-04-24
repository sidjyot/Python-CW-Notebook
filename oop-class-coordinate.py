class Coordinate(object):
  def __init__(self, a, b):
    self.x = a
    self.y = b
  def __str__(self):
    return f'(X={self.x}, Y={self.y})'

  def distance(self, other):
    x_diff_sq = (self.x - other.x) ** 2
    y_diff_sq = (self.y - other.y) ** 2
    dist = (x_diff_sq + y_diff_sq) ** 0.5
    return dist
    
   
c1 = Coordinate(4,5)
c2 = Coordinate(8,9)
#Accessing via object c1 or c2
print(round(c2.distance(c1)))
#Accessing via class directly
print(round(Coordinate.distance(c1, c2)))


