# integer = [1, 2, 3, 4]
nums = input("숫자 리스트:")
finding_num = int(input("찾고싶은 정수:"))

nums = list(map(int, nums.split()))

if finding_num in nums:
 print(finding_num, "은 리스트에 포함되어 있습니다.")
else:
 print("없습니다.")