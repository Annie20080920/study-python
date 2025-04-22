import os

old_name = input("기존 파일명:")
new_name = input("새로운 파일명:")

os.rename("old_name", "new_name")
print("파일명 변경 완료")