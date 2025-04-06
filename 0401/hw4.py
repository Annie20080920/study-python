numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
odd_count = 0
even_count = 0

for num in numbers:
  if num % 2 == 1:
    odd_count = odd_count+1
  else:
    even_count = even_count+1

print("홀수 개수:", odd_count)
print("짝수 개수:", even_count)