# Q1.1
class BankAccount:
  def __init__(self, balence, name, account_number):
    self.balence = balence
    self.name = name
    self.account_number = account_number
  # def get_account_number(self):
  #   retrun self.account_number
  def use_atm(self, atm: ATM):
    print(f"{self.name} is using the ATM.")
    print("Current Balence:", atm.balence)
   
  def deposit(self, amount):
    amount = float(input("Enter deposit amount:"))
    self.balence = self.balence + amount
  def withdraw(self, amount):
    amount = float(input("Enter withdrawl amount:"))
    if self.balence - amount >= 0:
      self.balence = self.balence - amount
  def get_balence(self):
    return self.balence