def isPalindrome(n):
    copy = 0
    stored = []
    j = 0
    tracker = 0
    while copy < n:
        nums = n % 10**j
        if nums > 0:
            x = (nums - copy) // 10**(j - 1)
            copy = nums
            stored.append(x)
        j += 1
        tracker = n - copy
        if n - tracker != copy:
            return False
    i = len(stored) - 1
    for el in stored:
        if el != stored[i]:
            return False
        else:
            i -= 1
    return True
