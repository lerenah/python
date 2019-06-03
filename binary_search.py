def binarySearch(array, target):
    # Write your code here.
	low = 0
	high = len(array) - 1
	while low <= high:
		middle = (low + high) // 2
		if target == array[middle]:
			return middle
		elif target < array[middle]:
			high = middle - 1
		elif target > array[middle]:
			low = middle + 1
	return -1
