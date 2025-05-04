fruits = ["사과", "바나나"]
colors = ["빨강", "노랑"]

result = [f"{color} {fruit}" for color in colors for fruit in fruits]
print(result)