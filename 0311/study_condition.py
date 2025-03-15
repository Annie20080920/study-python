num = input()
if int(num) < 0:
 print("음수")
elif int(num) > 0:
 print("양수")
else:
 print("0")

 password = input()
if password == "python123":
  print("True")
else:
  print("False")

number = input()
if int(number) % 2 ==0:
 print("even")
elif int(number) % 2 ==1:
 print("odd")

grade = input()
if int(grade) >= 90:
 print("A")
elif 80<= int(grade):
 print("B")
elif 70 <= int(grade):
 print("C")
else:
 print("F")