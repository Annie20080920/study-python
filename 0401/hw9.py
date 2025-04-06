A = [1, 2]
B = [3, 4]
def cartesian_product(A, B):
  result = []
  for a in A:
    for b in B:
      result.append((a, b))
    return result

print(cartesian_product(A, B))
