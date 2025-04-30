class Account:
  def __init__(self, accountnumber, name, balence):
    self.accountnumber = accountnumber
    self.name = name
    self.balence = int(balence)

  def deposit(self, amount):
    self.balence += amount
  
  def withdraw(self,amount):
    if amount > self.balence:
      print("잔액이 부족합니다.")
    else:
      self.balence -= amount
  
  def get_balence(self):
    return self.balence

    
    
