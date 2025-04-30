import collections

text = input("문자열을 입력하세요:")
lower_text = text.lower()

# list comprehensive
filtered_text = [word for word in lower_text if word.isalpha()]
 
for letter, num in collections.Counter(filtered_text).items():
  print(letter, num, sep=":")