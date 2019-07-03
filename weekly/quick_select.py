def quick_select(arr, k):
  return quick_select_helper(arr, 0, len(arr) - 1, k)

def quick_select_helper(arr, start, end, k)
  index = find_pivot(arr)
  if index == k - 1:
    return arr[index]
  elif index < (k - 1):
    quick_select(arr[:index])
  elif index > (k - 1):
    quick_select(arr[index:])
return -1
