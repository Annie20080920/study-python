class PasswordChecker:
  def check(self):
    while True:
      self.password = input("비밀번호를 입력하시오.")

      if self.password == "python123":
        break
        
pc = PasswordChecker()
pc.check()
