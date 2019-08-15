def sorted_bit_search(arr):
  target = 1
  def helper(a, target):
    high, low = len(a) - 1, 0
    while low <= high:
      mid = (high + low) // 2
      if a[mid] == target:
        if a[mid - 1] == target:
          high = mid - 1
        else:
          return len(a) - mid
      else:
        low = mid + 1
  count = helper(arr, target)
  return count

arr1 = [0,0,0,0,0,1,1,1] # 3
arr2 = [0, 1, 1, 1 ,1 ,1, 1] # 6
print(sorted_bit_search(arr1))
print(sorted_bit_search(arr2))
