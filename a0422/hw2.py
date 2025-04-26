import datetime

birth = input("생년월일 입력(YYYY-MM-DD):")
birth_date = datetime.datetime.strptime(birth, "%Y-%m-%d")

today = datetime.datetime.today()

age = today.year - birth_date.year

if today.month < birth_date.month:
  age -= 1
elif today.month == birth_date.month and today.day < birth_date.day:
  age -= 1
  
print(f"당신의 만 나이는 {age}세입니다.")
