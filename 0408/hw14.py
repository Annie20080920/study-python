class Rectangle:
  def __init__(self, width, height):
    self.width = width
    self.height = height

  def area(self):
    print("넓이:", self.width * self.height)
    
rectangle = Rectangle(10, 20)
rectangle.area()