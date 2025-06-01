class Flyable:
  def fly(self):
    print("나는 날 수 있어요!")

class Swimmable:
  def swim(self):
    print("나는 수영할 수 있어요!")

class Duck(Flyable, Swimmable):
  pass

duck = Duck()
duck.fly()
duck.swim()