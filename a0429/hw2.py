def make_double():
  numbers = [1, 3, 5, 7, 9]
  result= [n * 2 for n in numbers if n > 5]
  print(result)

make_double()