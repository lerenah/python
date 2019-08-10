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
