import hw6_module

option = input("변환 종류를 선택하세요 (1: C→F, 2: F→C):")

if option == "1":
  celsius = float(input("온도 입력 (섭씨):"))
  result = hw6_module.c_to_f(celsius)
  print(f"변환된 온도: {result:.1f}°F")

elif option =="2":
  fahrenheit = float(input("온도 입력 (화씨): "))
  result = hw6_module.f_to_c(fahrenheit)
  print(f"변환된 온도: {result:.1f}°C")

else:
  print("잘못된 입력입니다. 1 또는 2를 입력해주세요.")