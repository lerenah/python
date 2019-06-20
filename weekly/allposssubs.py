arr = ['a', 'b', 'c', 'd']
# look at first el in arr


def sets(arr):
  if len(arr) == 0:
    return [[]]
  subs = [arr[0]]
  rest = arr[1:]
  newArr = sets(rest)
  first = list(map(lambda x: subs[x], newArr))

  return [newArr.extend(first)]
