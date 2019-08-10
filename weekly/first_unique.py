def firstUniqChar(self, s):
    """
    :type s: str
    :rtype: int
    """
    from collections import Counter
    if not len(s):
        return -1
    seen = Counter(s)
    indices = []
    for key, val in seen.items():
        if val == 1:
            indices.append(s.index(key))
    if len(indices):
        return min(indices)
    return -1
