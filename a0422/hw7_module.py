class Book:

  def __init__(self, title, author, ISBN):
    self.title = title
    self.author = author
    self.ISBN = ISBN

  def output(self):
    return f"제목: {self.title}, 저자: {self.author}, ISBN: {self.ISBN}"