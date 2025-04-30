class Book:

  def __init__(self, title, author, isbn):
    self.title = title
    self.author = author
    self.isbn = isbn

  def output(self):
    return f"제목: {self.title}, 저자: {self.author}, ISBN: {self.ISBN}"