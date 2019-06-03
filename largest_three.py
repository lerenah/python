def findThreeLargestNumbers(array):
	sortedArr = []
	while len(sortedArr) < 3:
		largest = array[0]
		for num in array:
			if num >= largest:
				largest = num
		sortedArr.append(largest)
		array.remove(largest)
	sortedArr2 = sorted(sortedArr)
	return sortedArr2
