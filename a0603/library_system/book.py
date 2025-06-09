class Book:
  def __init__(self, title, author, available = True):
    self.title = title
    self.author = author
    self.available = available
   
  def __str__(self):
    if self.available:
      status = "대여 가능" 
    else:
      status = "대여 중"

    return f"[{status}] {self.title} - {self.author}"
    
