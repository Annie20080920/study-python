#------------------------
class Cave:
  def __init__(self, name, description):
    self.name = name
    self.description = description
    self.linked_caves = {}
    self.character = None
    self.item = None

  # def create_cave(name, description):
  #   return {
  #     'name': name,
  #     'description': description,
  #     'linked_caves': {},
  #     'character': {},
  #     'item': None
  #   }
  
  def set_description(self, description):
    self.description = description
  
  def get_description(self):
    return self.description

  def link_caves(self, cave2, direction):
    direction_opposites = {
      'north': 'south',
      'south': 'north',
      'east': 'west',
      'west': 'east'
    }
    self.linked_caves[direction] = cave2
    cave2.linked_caves[direction_opposites[direction]] = self
    
  def get_name(self):
    return self.name

  def describe_cave(self):
    print(self.description)
    for direction, cave in self.linked_caves.items():
      print(f"The {cave.name} is {direction}")

  def move_cave(self, direction):
    if direction in self.linked_caves:
      return self.linked_caves[direction]
    else:
      print("You can't go that way")
      return self
  
  def set_character(self, character):
    self.charcter = character

  def get_character(self):
    return self.charcter

  def set_item(self, item):
    self.item = item

  def get_item(self):
    return self.item
    
# def create_enemy(name, description, conversation, weakness):
#   return {
#     'name': name,
#     'description': description,
#     'conversation': conversation,
#     'weakness': weakness,
#     }

class Enemy:
  def __init__(self, name, description, conversation, weakness):
    self.name = name
    self.description = description
    self.conversation = conversation
    self.weakness = weakness
  
  def describe_enemy(self):
    print(f"{self.name} is here!")
    print(self.description)
  
  def fight_enemy(self, item):
    if item == self.weakness:
      print(f"You fend {self.name} off with the {item}")
      return True
    else:
      print(f"{self.name} swallows you, little wimp")
      return False

  def steal_from_enemy(self):
    print(f"You steal from {self.name}")
# def create_friend(name, description, conversation):
#   return {
#     'name': name,
#     'description': description,
#     'conversation': conversation,
#     }

class Friend():
  def __init__(self, name, description, conversation):
    self.name = name
    self.description = description
    self.conversation = conversation
  
  def describe_friend(self):
    print(f"{self.name} is here!")
    print(self.name)
#------------------------
class Item:
  def __init__(self, name, description):
    self.name = name
    self.description = description
  def describe_item(self):
    print(f"The [{self.name}] is here - {self.description}")

#Create caves
cavern = Cave("cavern"," A damp and dirty cave.")
grotto = Cave("Grotto", " A small cave with ancient graffiti.")
dungeon = Cave("Dungeon", " A large cave with a rack")

# # names of caves
# cavern_name = "Cavern"
# grotto_name = "Grotto"
# dungeon_name = "Dungeon"

# # create cave instances
# cavern = create_cave(cavern_name, cavern_description)
# grotto = create_cave(grotto_name, grotto_description)
# dungeon = create_cave(dungeon_name, dungeon_description)

# link the caves
cavern.link_caves(grotto, 'west')
cavern.link_caves(dungeon, 'north')
dungeon.link_caves(grotto, 'east')

# set_description(cavern, cavern_description)
# set_description(grotto, grotto_description)
# set_description(dungeon, dungeon_description)
# # create characters
harry = Enemy(
  name = "Harry", 
  description = "A smelly Wumpus",
  conversation = "Hangry…Hanggrry",
  weakness = "vegemite"
)

josephine = Friend(
  name = "Josephine", 
  description = "A friendly bat",
  conversation = "Gidday.",
)

# Place characters
dungeon.set_character(harry)
grotto.set_character(josephine)

# Create items
vegemite = Item("vegemite", "A Wumpuses worst nightmare")
torch = Item("torch", "A light for the end of the tunnel")

grotto.set_item(vegemite)
dungeon.set_item(torch)



# game state
bag = []
current_cave = cavern
dead = False

# not needed variables(didn't use it in the game code) 
# direction_opposites = {
#     'north': 'south',
#     'south': 'north',
#     'east': 'west',
#     'west': 'east'
#     }
# }

# game loop
while not dead:
  print("\n")
  current_cave.describe_cave()

  character = current_cave.get_character()
  if character:
    if isinstance(character, dict) and 'conversation' in character:
      Enemy.describe_enemy(character)
    elif isinstance(character, dict):
      Friend.describe_friend(character)

  item = current_cave.get_item()
  if item:
    Cave.describe_item(item)

  command = input(">")

  if command in ['north', 'south', 'east', 'west']:
    current_cave = current_cave.move_cave(command)

  elif command == "talk":
    character = current_cave.get_character()
    if character and isinstance(character, dict) and 'conversation' in character:
      print(f"[{character['name']} says]: {character['conversation']}")

  elif command == "fight":
    character = current_cave.get_character()
    if character and isinstance(character, dict) and 'weakness' in character:
      print("What will you fight with?")
      
      fight_with = input()
      if fight_with in bag:
        # 
        if Enemy.fight_enemy(character, fight_with, current_cave):
          print("Bravo, hero you won the fight!")
          current_cave.set_character(None)
          
          if len(bag) == 0:
            print("Congratulations, you have survived another adventure!")
            
          dead = True
                
        else:
          print("Scurry home, you lost the fight.")
          print("That's the end of the game")
          dead = True
      else:
          print(f"You don't have a {fight_with}")
    else:
        print("There is no one here to fight with")
# 
  elif command == "pat":
    character = current_cave.get_character()
    if character and isinstance(character, dict) and 'weakness' not in character:
      print(f"{character['name']} pats you back!")
    else:
      print("There is no one here to pat :(")
    
  elif command == "take":
    item = current_cave.get_item()

    if item:
      print(f"You put the {item['name']} in your bag")
      
      bag.append(item['name'])
      current_cave.set_item(None)


