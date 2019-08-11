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

    # alternative solution

    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        res = 0
        for i, num in enumerate(nums[:-2]):
            k = i + 2
            for j in range(i + 1, len(nums) - 1):
                if nums[i] == 0:
                    continue
                while k < len(nums) and (nums[i] + nums[j]) > nums[k]:
                    k += 1
                res += k - j - 1
        return res
