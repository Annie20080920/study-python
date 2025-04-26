import collections

text = input("문자열을 입력하세요:")
text1 = text.lower()
filtered_text = []
for i in text1:
  if i.isalpha():
     filtered_text.append(i)
 
print(collections.Counter(filtered_text))