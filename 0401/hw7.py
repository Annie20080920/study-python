nums = [1, 2, 3]
def get_subsets(nums):
  result = []
  result.append([])

  for num in nums:
    result.append([num])
  
  for num1 in nums:
    for num2 in nums:
      if num1 < num2:
        result.append([num1, num2])
  
  result.append(nums)

  return result

print(get_subsets(nums))