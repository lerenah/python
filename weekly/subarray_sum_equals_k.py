def subarraySum(nums, k):
  """
  :type nums: List[int]
  :type k: int
  :rtype: int
  """
  if not len(nums):
      return 0
  if len(nums) == 1 and k != nums[0]:
      return 0
  if len(nums) == 1 and k == nums[0]:
      return nums[0]
  res = 0
  total = 0
  totals = {0: 1}
  for end, num in enumerate(nums):
      total += num
      if total - k in totals:
          res += totals[total - k]
      if total in totals:
          totals[total] += 1
      else:
          totals[total] = 1
  return res
