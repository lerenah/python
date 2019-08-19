def numberOfArithmeticSlices(self, a):
  """
  :type A: List[int]
  :rtype: int
  """
  if len(a) < 3:
    return 0
  start, end = 0, 1
  res = 0
  check = []
  curr = abs(a[start] - a[end])
  while end + 1 in range(1, len(a)):
    diff = abs(a[end] - a[end + 1])
    if abs(diff - curr) != 0:
        start += 1
        # reset curr to compare new start
        curr = diff
        continue
    if (end - start) + 1 == 3:
        res += 1
        check.append(a[start])
        start += 1
        curr = abs(a[start] - a[end])
        continue
    end += 1
  if (end - start) + 1 == 3:
    check.append(a[start])
    res += 1
  if check == a[:-2] and len(a) > 3:
    res += 1

  return res

# solution
def numberOfArithmeticSlices(self, a):
  """
  :type A: List[int]
  :rtype: int
  """
  count, _sum = 0, 0
  for i in range(2, len(a)):
      if a[i] - a[i - 1] == a[i-1] - a[i - 2]:
          count += 1
      else:
          _sum += (count + 1) * (count) / 2
          count = 0

  _sum += count * (count + 1) / 2
  return _sum
