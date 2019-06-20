arr = ['a', 'b', 'c']
# look at first el in arr

subs = []

def add_to_subs(el):
  subs.append(el)



def sets(arr):
  for el in arr:
     add_to_subs(el)

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
