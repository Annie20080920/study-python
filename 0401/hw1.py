numbers = [1,2,3,4,5,6,7,8,9]

odd_numbers = []
even_numbers = []

for num in numbers:
  if num % 2 == 1:
    odd_numbers.append(num)
  else:
    even_numbers.append(num)
  
print("홀수 리스트:", odd_numbers)
print("짝수 리스트:", even_numbers)
                  