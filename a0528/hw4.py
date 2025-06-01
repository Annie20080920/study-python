class Shape:
  def draw(self):
    pass

class Circle(Shape):
  def draw(self):
    print("원을 그립니다")
   
class Square(Shape):
  def draw(self):
    print("정사각형을 그립니다")

shapes = [Circle(), Square(), Circle()]
for s in shapes:
  s.draw()