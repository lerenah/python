def pivotIndex(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if len(nums) == 0:
        return -1
    left = 0
    total = sum(nums)
    for i, el in enumerate(nums):
        if left == total - left - el:
            return i
        else:
            left += el
    return -1
