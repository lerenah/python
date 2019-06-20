arr = ['a', 'b', 'c']
# look at first el in arr

subs = []

def sets(arr):
  for el in arr:
     subs.append(el)

  if len(subs) == len(arr):
    newArr = []
    for i in subs:
      s = list(filter(lambda x: x != i, arr))
      s = ''.join(s)
      newArr.append(s)

  subs.extend(newArr)
  subs.append([])
  subs.append(''.join(arr))


  return subs
