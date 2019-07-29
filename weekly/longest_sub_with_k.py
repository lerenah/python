def longest_substring_with_k_distinct(str, k):
    start = 0
    cache = {}
    longest = 0
    for end in range(len(str)):
        el = str[end]
        if el not in cache:
            cache[el] = 0
        cache[el] += 1


        while len(cache.keys()) > k:
            end_el = str[start]
            cache[end_el] -= 1
            if cache[end_el] == 0:
                del cache[end_el]
            start += 1
        longest = max(longest, end - start + 1)
    return longest
