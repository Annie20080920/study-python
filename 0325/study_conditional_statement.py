num = int(input())
match num:
  case 1:
    print("하나")
  case 2:
    print("둘")
  case 3:
    print("셋")
  case _:
    print("알 수 없는 숫자")

def check_list_length(num):
  match num:
   case []:
    print("리스트가 비어있습니다.")
   case [x]:
    print("하나의 요소가 있습니다.")
   case [x, y]:
    print("두개의 요소가 있습니다.")
   case _:
    print("여러 개의 요소가 있습니다.")

check_list_length([1])

# person = {"name" : "Alice", "age" : 25, }
def is_exist(person):
 match person:
   case {"name": name, "age": age}:
    print(f"이름:{name} , 나이:{age}")
   case {"name": name}:
    print(f"이름: {name}, 나이는 없음")
   case {"age": age}:
    print(f"이름 없음, 나이:{age}")
   case _:
    print("이름과 나이응 알 수 없음")
is_exist({"name": "Alice", "age": 25})

    
