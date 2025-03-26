student = input()
student2 = input()
dictionary = {"Alice":"85", "Bob":"90"}
if student in dictionary:
 print(student, "님의 점수:", dictionary["Alice"])
 print(student2, "님의 점수:", dictionary["Bob"])
else:
 print(student, "은 존대하지 않습니다.")