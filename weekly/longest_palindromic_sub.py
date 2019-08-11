def longestPalindrome(self, s):
  """
  :type s: str
  :rtype: str
  """
  if not len(s):
      return 0
  if len(s) == 1:
      return 1
  length = 1
  output = s[0]
  left_curr = 0
  right_curr = 0
  matched = False
  for i in range(len(s)):
      if i == 0:
          left_curr = 0
          right_curr = i + 1
      if i == len(s) - 1:
          left_curr = i - 1
          right_curr = i
      else:
          left_curr = i - 1
          right_curr = i + 1
      if s[left_curr] == s[right_curr]:
          matched = True
          while matched:
              length = max(length, (right_curr - left_curr) + 1)
              output = s[left_curr: right_curr + 1]
              left_curr -= 1
              right_curr += 1
              if s[left_curr] != s[right_curr]:
                  matched = False
  return output


  # alternative
  def longestPalindrome(s):
    if s is '':
        return s
    max_len = 0
    start, end = 0, 0
    for i in range(len(s)):
        len1 = expandFromCenter(s, i, i)
        len2 = expandFromCenter(s, i, i + 1)
        l = max(len1, len2)
        if l > end - start:
            start = i - (l - 1) // 2
            end = i + l // 2

    return s[start:end + 1]


def expandFromCenter(s, idx1, idx2):
    while idx1 >= 0 and idx2 < len(s) and s[idx1] == s[idx2]:
        idx1 -= 1
        idx2 += 1
    return idx2 - idx1 - 1
