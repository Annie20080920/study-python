# class Animal:
#   def __init__(self,name):
#     self.name = name

#   def speak(self):
#     print("animal")

# class Dog(Animal):
#   def speak(self):
#     print(f"멍멍! 나는 {self.name}야")

# d = Dog("초코")
# d.speak()

# class Animal:
#   def speak(self):
#     print("")

#   def info(self):
#     print("나는 동물입니다")

# class Dog(Animal):
#   def speak(self):
#     print("멍멍!")
  
# class Cat(Animal):
#   def speak(self):
#     print("야옹~")
 
# class Bird(Animal):
#   def speak(self):
#     print("짹짹!")

# for animal in [Dog(), Cat(), Bird()]:
#   animal.speak()
#   animal.info()

class Shape:
  def __init__(self, name):
    self.name = name

  def describe(self):
    print(f"{self.name} 입니다.")

class Circle(Shape):
  def __init__(self, radius):
    self.radius = radius
    super().__init__("원")

  def area(self, radius):
    return radius**2 * 3.14
  
class Rectangle(Shape):
  def __init__(self, width, height):
    self.width = width
    self.height = height
    super().__init__("직사각형")
  
  def area(self, width, height):
    return width * height
  
circle = Circle(3)
circle.describe()
print(circle.area(3))

rectangle = Rectangle(4, 5)
rectangle.describe()
print(rectangle.area(4,5))
  

 