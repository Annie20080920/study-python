from hw8_module import Account

print("계좌 생성")
name = input("이름:")
account_number = input("계좌번호:")
initial_balence = input("초기 입금액:")

account = Account(name, account_number, initial_balence)

while True:
  print("1: 입금, 2: 출금, 3: 잔액조회, 0: 종료")
  choice = input("선택:")

  if choice == "1":
    amount = int(input("금액 입력:"))
    account.deposit(amount)

  elif choice == "2":
    amount = int(input("금액 입력:"))
    account.withdraw(amount)

  elif choice == "3":
    print(f"현재 잔액: {account.get_balence()}원")
  
  elif choice == "0":
    break

  else:
    print("올바른 선택이 아닙니다.")
