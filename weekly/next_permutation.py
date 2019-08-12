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

# in place solution


def nextPermutation(self, nums):
    """
    :type nums: List[int]
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    def reverse(a, start, end):
        while start <= end:
            swap(a, start, end)
            start += 1
            end -= 1

    def swap(a, i, j):
        a[i], a[j] = a[j], a[i]

    if len(nums) == 0:
        return 0
    i = len(nums) - 1

    while i - 1 >= 0 and nums[i - 1] > nums[i]:
        i -= 1
    if i < 0:
        return reverse(nums, i, len(nums) - 1)
    reverse(nums, i, len(nums) - 1)
    swap(nums, i, i - 1)

    # alternative
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        for i in range(len(num) - 2, -1, -1):
            for j in range(len(num) - 1, i, -1):
                if num[i] < num[j]:
                    num[i], num[j] = num[j], num[i]
                    num[i+1:] = num[i+1:][::-1]
                    return

    num.reverse()
