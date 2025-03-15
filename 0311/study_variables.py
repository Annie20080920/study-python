str1= "Hello"
num1= 5
str2= str(num1)
result1= str1+str2
print(result1)

num1=5
str1="10"
num2=int(str1)
result1= num1+num2
print(result1)

count= 0
def increasement():
 global count
 count= count+1
 print(count)

increasement()

result = 0
num1 = input()
num2 = input()

def plus():
 print(f" num1 + num2 = {result}")
plus()

age = input("나이를 입력하세요")
name = input("이름을 입력하세요")
print("나의 이름은", name,"이고", "나이는", age, "살입니다.")