class Bird:
  def fly(self):
    print("새가 납니다")

class Penguin(Bird):
  def fly(self):
    print("펭귄은 날 수 없습니다")

p = Penguin()
p.fly()