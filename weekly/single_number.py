def singleNumber(self, nums):
  """
  :type nums: List[int]
  :rtype: int
  """
  from collections import Counter
  cache = Counter(nums)
  for key, val in cache.items():
      if val == 1:
          return key


# optimal solution
  res = 0
  for num in nums:
    res = res^num
  return res
