def print_hourglass(n):
  if n % 2 == 1:
    for i in range(n, 0, -2):
      print(" " * ((n-i) // 2) + "*" * i)
    for i in range(n-2, n+1, 2):
      print(" " * ((n-i) // 2) + "*" * i)

n = int(input())
print_hourglass(n)