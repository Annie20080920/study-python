import datetime

days = datetime.datetime.today().weekday()
weekdays = ["월요일", "화요일", "수요일", "목요일", "금요일", "토요일", "일요일"]
print(f"오늘은 {weekdays [days]}입니다.")