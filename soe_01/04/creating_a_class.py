class book:
 def _init_(self, title, author, year, genre, is_available):
  self.title = str(title)
  self.author = str(author)
  self.year = int(year)
  self.genre = str(genre)
  self.is_available = True

def borrow(self):
 if self.is_available:
    self.is_avilable = False
 else:
  print("Already borrowed")

def return_book(self):
 if ! self.is_avilable =
  self.is_avilable = True
 else:
  print("Already borrowed")

class phone():
  def is_Ringing(self):
    pass
class HomePhone():  
  def __init__(self, brand, model, operating_system, storage, battery_level):
    self.brand = str(brand)
    self.model = str(model)
    self.operating_system = str(operating_system)
    self.storage = float(storage)
    self.battery_level = float(battery_level)
    power:bool = False
    app_name = []

class mobilephone(phone):
  def power_on(self):
    if power == False:
      power = True
      print("Power on")
def power_off():
  if power == True:
    power = False
    print("Power off")

def install_app(self, name, size):
  if name in app_name:
    print("Already installed")
  else:
    if storage - size < 0:
      print("Nor enough space")
    else:
      print(f"App{name} installed")
      storage == size
      app_name.append(name)