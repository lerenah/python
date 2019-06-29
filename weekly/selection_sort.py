def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp



def selectionSort(array):
    for i in range(len(array) - 1):
        j = i + 1
        min = array[i]
        min_j = j
        while j in range(len(array)):
            if array[j] < min:
                min = array[j]
                min_j = j
            j += 1
        if min < array[i]:
            swap(array, i,min_j)
