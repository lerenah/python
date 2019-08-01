def fruits_into_baskets(fruits):
  # TODO: Write your code here
  fruit_types = {}
  total = 0
  count = 0
  for fruit in fruits:
    if fruit not in fruit_types:
      fruit_types[fruit] = 0
    fruit_types[fruit] += 1

  maximum = sorted(list(fruit_types.values()))
  for key, val in fruit_types.items():
    if val == maximum[-1]:
      total += maximum.pop()
      count += 1
      if count == 2:
        break

  return total
