def search_ceiling_of_a_number(arr, key):
  # TODO: Write your code here
  high, low = len(arr) - 1, 0
  while low <= high:
    mid = (high + low) // 2
    if arr[mid] == key:
      return arr[mid]
    if arr[mid] > key:
      high = mid - 1
    else:
      low = mid + 1
  if mid < low:
    return -1
  if mid > high:
    return arr[mid]


  return 0
