class Book:
  pass
class Movie:
  pass

for x in [Book(), Movie(), Book()]:
  if isinstance(x, Book):
    print("책입니다")

  elif isinstance(x, Movie):
    print("영화입니다")