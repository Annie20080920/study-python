file_name = input("파일이름을 입력하세요.")
numbers = []
try:
  file = open("a0603/" + file_name, "r")
  
  lines = file.readlines()
  for line in lines:
    line = (line.strip())
    try:
      number = float(line)
      numbers.append(number)
    except ValueError:
      print("숫자가 아닌 값이 포함되어있습니다.")
      break
  else:
    print(sum(numbers) / len(numbers))

except FileNotFoundError:
  print("파일이 존재하지않습니다.")

finally:
  file.close()
  print("파일 닫힘")