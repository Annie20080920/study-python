import datetime

input_date = input("날짜 입력 (YYYY-MM-DD):")
date = datetime.datetime.strptime(input_date, "%Y-%m-%d")
weekday_num = date.weekday()

weekdays = ["월요일", "화요일", "수요일", "목요일", "금요일", "토요일", "일요일"]
weekday = weekdays[weekday_num]

if weekday_num >= 5:
  print(f"해당 날짜는 {weekday}이며, 주말입니다.")
else:
  print(f"해당 날짜는 {weekday}이며, 평일입니다.")