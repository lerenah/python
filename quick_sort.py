import random


def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


def quick_sort(arr):
    quick_sort_helper(arr, 0, len(arr) - 1)


def quick_sort_helper(arr, start, end):
    if start >= end:
        return arr

    random_idx = random.randint(start, end)
    pivot = arr[random_idx]
    smaller = start
    bigger = start
    swap(arr, random_idx, start)
    for bigger in range(start + 1, end + 1):
        if arr[bigger] < pivot:
            smaller += 1
            swap(arr, smaller, bigger)
    swap(arr, start, smaller)
    quick_sort_helper(arr, start, smaller - 1)
    quick_sort_helper(arr, smaller + 1, end)
    return arr
