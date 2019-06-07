def expansion(str):
    scale = 0
    contents = ''
    start_idx = str.index('[') - 1
    stop_idx = str.index(']')
    str_to_int = int(str[start_idx])
    if type(str_to_int) == int:
        while scale in range(str_to_int):
            contents += str[start_idx + 2:stop_idx]
            scale += 1
    return contents

print(expansion('3[a]'))

str = '3[a]'
arr = []
opened = []
closed = []
final_str = ''

for idx, el in enumerate(str):
  arr.append(el)
  if el == '[':
    opened.append(idx)
  elif el == ']':
    closed.append(idx)

# use recursion

lidx = 0
ridx = len(opened) - 1
while lidx != ridx:
  opening = opened[ridx]
  closing = closed[lidx]
  print(opening)
  print(closing)
  num = int(arr[opening - 1])
  for i in range(num):
    final_str += str[opening + 1: closing]
  lidx += 1
  ridx -= 1
