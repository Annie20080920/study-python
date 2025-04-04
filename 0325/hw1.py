def check_person_info(person):
 match person:
   case {"name": name, "age": age}:
    return(f"이름:{name} , 나이:{age}")
   case {"name": name}:
    return(f"이름: {name}, 나이는 없음")
   case {"age": age}:
    return(f"이름 없음, 나이:{age}")
   case _:
    return("이름과 나이를 알 수 없음")
  
# check_person_info(person)
print(check_person_info({"name": "Alice", "age": 25}))
# {"name": "Alice", "age": 25}
# {"name": "Bob"}
# {"age": 30}
# {"height": 180}