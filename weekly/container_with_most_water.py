def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height) == 2:
            return min(height)
        maxes = []
        i = 0
        while i + 1 in range(len(height)):
            if height[i] >= height[i + 1]:
                maxes.append(height[i])
            else:
                maxes.append(height[i + 1])
            i += 1
        minimum = maxes[0] if maxes[0] < maxes[-1] else maxes[-1]
        return minimum * (len(maxes)- 1)



# alternative
def maxArea(self, height):
    """
    :type height: List[int]
    :rtype: int
    """
    max_area = 0
    start, end = 0, len(height) - 1
    while start < end:
        max_area = max(max_area, min(height[start], height[end]) * (end - start))
        if height[start] > height[end]:
            end -= 1
        else:
            start += 1
    return max_area
