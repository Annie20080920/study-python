number = int(input())
if number % 2 == 0:
  if number > 10:
    print("10보다 큰 짝수")
  elif number < 10:
    print("10이하의 짝수")
else:
  print("홀수")