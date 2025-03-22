amount = int(input())
membership_grade = str(input("VIP or 일반"))
if membership_grade == "VIP":
  if amount >= 100000:
    print("최대 할인 적용")
  else:
    print("추가 구매 필요")
elif membership_grade == "일반":
   print("기본 할인 적용")