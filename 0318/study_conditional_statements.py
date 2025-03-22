id = input("아이디를 입력하시요.")
password = input("비밀번호를 입력하시요.")

if id == "admin" and password == "1234":
 print("로그인 성공!")
if id == "admin" and password != "1234":
  print("비밀번호가 틀렸습니다.")
elif id != "admin":
 print("아이디가 존재하지 않습니다.")

num = int(input())
if num > 0:
 if num < 10:
  print("0보다 크고 10보다 작습니다.")
 elif num >10:
  print("10 이상입니다")
else:
 print("0 이하입니다.")