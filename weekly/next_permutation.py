class Solution(object):
  def nextPermutation(self, nums):
      """
      :type nums: List[int]
      :rtype: None Do not return anything, modify nums in-place instead.
      """
      if len(nums) == 0:
          return 0
      i = len(nums) - 1
      while i - 1 >= 0 and nums[i - 1] > nums[i]:
          i -= 1
      if i < 0:
          return nums[::-1]
      output = nums[:i] + list(reversed(nums[i:]))
      output[i], output[i - 1] = output[i - 1], output[i]
      return output
