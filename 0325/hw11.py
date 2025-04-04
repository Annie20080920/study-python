n = int(input("0보다 큰 정수를 입력하세요."))

if n > 0:
    for i in range(0, n): 
        print("*" * (n-i)) 
else:
    print("잘못된 입력입니다. 0보다 큰 정수를 입력하세요.")