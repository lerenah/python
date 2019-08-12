def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counter = nums[0]
        highest_seen = nums[0]
        for end in range(1, len(nums)):
            # check two conditions here; a is higher or a + b is higher
            if nums[end] > nums[end] + counter:
                counter = nums[end]
            else:
                counter += nums[end]
            # update highest seen
            if highest_seen < counter:
                highest_seen = counter

        return highest_seen

# update
def maxSubArray(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    counter = nums[0]
    highest_seen = nums[0]
    for end in range(1, len(nums)):
        # check two conditions here; a is higher or a + b is higher
        counter = max(counter + nums[end], nums[end])
        # update highest seen
        if highest_seen < counter:
            highest_seen = counter

    return highest_seen
