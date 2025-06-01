# class Parent:
#   def __init__(self, name):
#     self.name = name

#   def say_hello(self):
#     print("Hello from parent")

# class Child(Parent):
#   def __init__(self,name, age):
#     super().__init__(name)
#     self.age = age
  
#   def say_hello(self):
#     print(f"Hello {self.name}")

# c = Child("Alice")
# c.say_hello()

class Animal:
  def speak(self):
    print("animal")

class Dog(Animal):
  def speak(self):
    print("멍멍")

class Cat(Animal):
  def speak(self):
    print("야옹야옹")

class Bird(Animal):
  def speak(self):
    print("짹짹")

d = Dog()
d.speak()

c = Cat()
c.speak()

b = Bird()
b.speak()
