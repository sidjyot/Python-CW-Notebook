class Restaurant():
  '''A simple attempt to model a restaurant'''

  def __init__(self,restaurant_name, cuisine_type):
    """Initialize name and age attributes"""
    self.restaurant_name = restaurant_name
    self.cuisine_type = cuisine_type

  def describe_restaurant(self):
    """Describe the attributes of the restaurant"""
    print(self.restaurant_name.title() + " is a restaurant that serves " + self.cuisine_type.title() + " food!")

  def open_restaurant(self):
    """Indicate that the restaurant is Open"""
    print(self.restaurant_name.title() + " is open!")

restaurant = Restaurant('Manchurian Club', 'Indo-Chinese')
my_restaurant = Restaurant('Shahi Maharani', 'North Indian')
italian_restaurant = Restaurant('Prego', 'Italian')

#print("Restaurant's name is " + restaurant.restaurant_name.title() + ".")
#print("It serves " + restaurant.cuisine_type + " food.")
restaurant.describe_restaurant()
#restaurant.open_restaurant()
my_restaurant.describe_restaurant()
italian_restaurant.describe_restaurant()


