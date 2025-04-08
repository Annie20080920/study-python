def print_right_triangle(n):
  for i in range(1, n+1):
    print (" " * (n-i) + "*" * i)
  
n = int(input())
print_right_triangle(n)
