def merge(self, nums1, m, nums2, n):
  """
  :type nums1: List[int]
  :type m: int
  :type nums2: List[int]
  :type n: int
  :rtype: None Do not return anything, modify nums1 in-place instead.
  """

  n1_i = m - 1
  n2_i = n - 1
  end = len(nums1) - 1
  while n2_i >= 0 and n1_i >= 0:
      if nums1[n1_i] > nums2[n2_i]:
          nums1[end] = nums1[n1_i]
          n1_i -= 1
      else:
          nums1[end] = nums2[n2_i]
          n2_i -= 1
      end -= 1
  if n2_i >= 0:
      while n2_i >= 0:
          nums1[end] = nums2[n2_i]
          end -= 1
          n2_i -= 1

  return nums1
