from models.book import Book
from pathlib import Path
class Library:
  def __init__(self):
    self.books = []

  def add_book(self, title, author):
    for book in self.books:
        if book.title == title:
          print(f"책 '{title}'은(는) 이미 등록되어 있습니다.")
          return
    new_book = Book(title, author)
    self.books.append(new_book)
    print(f"책 '{title}'가 등록되었습니다.")

  def borrow_book(self, title):
    for book in self.books:
      if book.title == title:
        if book.available:
          book.available = False
          print(f"책 '{title}'를 대여했습니다.")
          
        else:
          print(f"책 '{title}'는 이미 대여 중입니다.")
          
        return
      else:
        pass
    print(f"책 '{title}'는 도서관에 존재하지 않습니다.")

  def list_books(self):
    for book in self.books:
      print(book)

  def load_books(self, filename):

    try:
      with open(Path(__file__).resolve().parent.parent/"data"/filename, "r") as file:
        for line in file:
          title, author, available_str = line.strip().split(",")
          available = (available_str == "True")
          self.books.append(Book(title, author, available))
        print("책 목록을 불러왔습니다.")
    except FileNotFoundError:
      print("파일이 존재하지 않습니다. 새로 시작합니다.")

  def save_books(self, filename):
    with open(Path(__file__).resolve().parent.parent/"data"/filename, "w") as file:
      for book in self.books:
        file.write(f"{book.title},{book.author},{book.available}\n")
    print("책 목록이 저장되었습니다.")
