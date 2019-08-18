class MovingAverage(object):

  def __init__(self, size):
      """
      Initialize your data structure here.
      :type size: int
      """
      self.sum = 0.0
      self.count = 0
      self.result = 0
      self.size = size
      self.q = []

  def next(self, val):
      """
      :type val: int
      :rtype: float
      """
      if self.count == self.size:
          self.sum -= self.q.pop(0)
          self.count -= 1
      self.q.append(val)
      self.sum += val
      self.count += 1
      self.result = self.sum / self.count
      return self.result



# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
