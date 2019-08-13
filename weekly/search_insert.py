def search(a, target):
  high = len(a) - 1
  low = 0
  while low <= high:
    mid = (high + low) // 2
    if a[mid] == target:
      return mid
    if a[mid] > target:
      high = mid - 1
    else:
      low = mid + 1

  # if high <= 0:
  #   high = 0
  #   while a[high] < target:
  #     high += 1
  #   return high
  # if low >= len(a) - 1:
  #   low = len(a) - 1
  #   while a[low] > target:
  #     low -= 1
  #   return low + 1
  
  if target > a[mid]:
    return mid + 1
  else:
    return mid


# alternative
def searchInsert(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    if target > nums[-1]:
        return len(nums)
    for i in range(len(nums)):
        if nums[i] >= target:
            return i
