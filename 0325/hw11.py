n = int(input("0보다 큰 정수를 입력하세요."))

if n > 0:
    for i in range(n, 0, -1): 
        print("*" * i) 
else:
    print("잘못된 입력입니다. 0보다 큰 정수를 입력하세요.")