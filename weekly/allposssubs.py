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
      for el in s:
        x = [i, el]
        z = sorted(x)
        y = ''.join(z)
        if y not in newArr:
          newArr.append(i + el)
      s = ''.join(s)
      if s not in newArr:
          newArr.append(s)

  subs.extend(newArr)
  subs.append([])
  subs.append(''.join(arr))


  return subs

