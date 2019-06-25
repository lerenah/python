arr = []
smallest = 9999999
second_smallest = 999999
index_smallest = 0
index_second = 0
for i, el in enumerate(arr):
  if el < smallest:
    second_smallest = smallest
    index_second = index_smallest
    smallest = el
    index_smallest = i
  if i != index_smallest:
    if el < second_smallest:
      second_smallest = el
      index_second = i
