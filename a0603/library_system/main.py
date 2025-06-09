from library import Library

lib = Library()
lib.load_books("data/book_data.txt")
lib.add_book("모모", "미하엘 엔데")
lib.borrow_book("모모")
lib.list_books()
lib.save_books("data/book_data.txt")