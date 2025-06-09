class Fruit:
  def info(self):
    pass
class Apple(Fruit):
  def info(self):
    return "나는 사과입니다."
class Banana(Fruit):
  def info(self):
   return "나는 바나나입니다."

items = [Apple(), Banana(), "hello", 123]

for item in items:
  if isinstance(item, Fruit):
    print(item.info())