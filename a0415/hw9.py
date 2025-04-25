class MultiplicationTable:
  def __init__(self, dan):
    self.dan = float(dan)

  def round_number(self):
    self.dan = round(self.dan)

  def is_valid_number(self):
    if self.dan > 1 and self.dan < 30:
      return True
    else:
      return False
      
  def print_table(self):
    print(f"< {self.dan}단 >")
    for i in range(1,10):
      print(f"{self.dan} * {i} = {self.dan * i}")
  
  def run(self):
    if self.is_valid_number():
      self.round_number()
      self.print_table()

user_input = input("단을 입력하세요 (1 < 단 < 30): ")

multiplication_table = MultiplicationTable(user_input)

multiplication_table.run()