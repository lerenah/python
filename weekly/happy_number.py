def isHappy(self, n):
  """
  :type n: int
  :rtype: bool
  """
  seen = [n]
  q = []
  while True:
      while n > 0:
          num = n % 10
          n -= num
          n //= 10
          q.append(num)

      while q:
          n += q.pop()**2
      if n == 1:
          return True
      if n not in seen:
          seen.append(n)
      else:
          return False
