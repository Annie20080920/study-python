day = input("요일을 입력하시요.")
match day:
  case ("월요일"):
    print(f"{day}: 오늘은 학교가는 날!")
  case ("화요일"):
    print(f"{day}: 오늘은 독서하는 날!")
  case ("수요일"):
    print(f"{day}: 오늘은 영화보는 날!")
  case ("목요일"):
    print(f"{day}: 오늘은 친구들과 저녁 약속!")
  case ("금요일"):
    print(f"{day}: 오늘은 코당 연습하는 날!")
  case ("토요일"):
    print(f"{day}: 오늘은 python 숙제 하는 날!")
  case ("일요일"):
    print(f"{day}: 오늘은 푹 쉬는 날!")
  case _:
    print("잘못된 입력입니다")
    
