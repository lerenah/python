def max_sub_array_of_size_k(k, arr):
  # TODO: Write your code here
  if len(arr) == 0:
    return 0
  elif len(arr) < k:
    return arr

  output = 0
  end = k
  total = 0
  start = 0
  for start in range(len(arr) - k + 1):
    total = sum(arr[start:end])
    if total > output:
      output = total
    end += 1
  return output
