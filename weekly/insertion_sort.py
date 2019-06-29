def insertionSort(array):
    # Write your code here.
	i = 0
	while i in range(len(array) - 1):
		j = i + 1
		if j in range(len(array)) and array[j] < array[j - 1]:
			while array[j] < array[j - 1] and j >= 1:
				temp = array[j]
				array[j] = array[j - 1]
				array[j - 1] = temp
				j -= 1
		i += 1
	return array
