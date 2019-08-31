def search_ceiling_of_a_number(arr, key):
    # TODO: Write your code here
    if key > arr[-1]:
        return -1

    start, end = 0, len(arr) - 1
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == key:
            return mid
        if key < arr[mid]:
            end = mid - 1
        else:
            start = mid + 1

    return start
