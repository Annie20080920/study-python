class BankAccount:
  def __init__(self, owner, balence):
    self.owner = owner
    self.balence = balence

  def deposit(self, amount):
    self.balence += amount
    print(f"입금 후 잔액: {self.balence}")
  
  def withdraw(self, amount):
    self.balence -= amount
    print(f"출금 후 잔액: {self.balence}")

  def get_balance(self):
    print(f"현재 잔액: {self.balence}")

bank_account = BankAccount("주영", 10000)
bank_account.deposit(10000)
bank_account.withdraw(500)
bank_account.get_balance()