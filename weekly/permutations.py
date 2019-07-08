def swap(arr, i, j):
  	arr[i], arr[j] = arr[j], arr[i]


def permutations(arr, n, acc):
	if n == len(arr) - 1:
		copy = arr[:]
		acc.append(copy)
		return copy
	for j in range(n, len(arr)):
		swap(arr, j, n)
		permutations(arr, n + 1, acc)
		swap(arr, j, n)

	return acc


def getPermutations(arr):
 	# Write your code here.
	perms = []
	permutations(arr, 0, perms)
	return perms
