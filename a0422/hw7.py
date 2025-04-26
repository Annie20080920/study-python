from hw7_module import Book

books = []

while True:
  title = input("제목: ")
  author = input("저자: ")
  isbn = input("ISBN: ")

  book = Book(title, author, isbn)
  books.append(book)

  add = input("책을 추가하시겠습니까? (y/n):")
  if add != "y":
    break

print("도서 목록:")
for book in books:
  print(book)