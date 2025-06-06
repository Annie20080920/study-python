class EvenOddCounter:
  def __init__(self, numbers):
    self.numbers = numbers

  def count(self):
    even_count = 0
    odd_count = 0

    for num in self.numbers:
      if num % 2 == 0:
        even_count += 1
      else:
        odd_count += 1

    print("짝수 개수:", even_count)
    print("홀수 개수:", odd_count)

even_odd_counter = EvenOddCounter()
even_odd_counter.count()