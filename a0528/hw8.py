class Animal:
  pass
class Cat(Animal):
  pass
class Dog(Animal):
  pass 

print(issubclass(Cat, Animal))
print(issubclass(Dog, Animal))
print(issubclass(int, Animal))
