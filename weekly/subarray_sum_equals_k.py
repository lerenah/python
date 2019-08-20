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



end, start = 0, 0 # 5, 1
length = float('inf') # 3
temp_sum = 0 # 12
while end in range(len(arr)):
  # if (end - start) + 1 >= length:
  #   start += 1
  temp_sum += arr[end]
  if temp_sum >= s:
    if (end - start) + 1 < length: # 2 - 0 = 3
      length = (end - start) + 1
      temp_sum -= arr[start]
      temp_sum -= arr[end]
      start += 1
      end -= 1
  end += 1

return length
