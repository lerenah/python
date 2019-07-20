def bubble_sort(array):
    swapped = False
    j = 1
    while not swapped:
        i = len(array) - 1
        swapped = True
        while i in range(j, len(array)):
            if array[i] < array[i - 1]:
                swap(array, i, i - 1)
                swapped = False
            i -= 1
        j += 1


def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]
