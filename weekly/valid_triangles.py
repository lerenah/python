def triangleNumber(self, nums):
  """
  :type nums: List[int]
  :rtype: int
  """
  copy = []
  copy = copy + nums
  triangles = 0
  sets = []
  for el in nums:
      copy.remove(el)
      i = 0
      if i + 1 in range(len(copy)):
          if el < (copy[i] + copy[i + 1]) and copy[i] < (el + copy[i + 1]) and copy[i + 1] < (el + copy[i]):
              sets.append([copy[i + 1], el, copy[i]])
              triangles += 1
      copy = []
      copy = copy + nums
  return triangles
