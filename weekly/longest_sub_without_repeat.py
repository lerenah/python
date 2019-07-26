def lengthOfLongestSubstring(self, s):
    """
    :type s: str
    :rtype: int
    """
    longest_seen = 0
    start = 0
    seen = {}
    for i, el in enumerate(s):
        if el in seen:
            start = max(start, seen[el] + 1)
        seen[el] = i
        longest_seen = max(longest_seen, i - start + 1)

    return longest_seen
