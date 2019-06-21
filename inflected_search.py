def search(arr, n):
    idx = -1
    left = 0
    right = len(arr) - 1
    mid = len(arr) // 2

    if n == arr[mid]:
        return mid

    # check for asc sort
    elif arr[left] < arr[mid] < arr[right]:
        if n < arr[mid]:
            if len(arr) <= 3:
                return mid - 1
            return search(arr[:mid], n)
        elif n > arr[mid]:
            if len(arr) <= 3:
                return mid + 1
            return search(arr[mid + 1:], n)

    # check for desc sort
    elif arr[left] > arr[mid] > arr[right]:
        if n < arr[mid]:
            if len(arr) <= 3:
                return mid + 1
            return search(arr[mid + 1:], n)
        elif n > arr[mid]:
            if len(arr) <= 3:
                return mid - 1
            return search(arr[:mid], n)

    # check for inflection
    elif arr[left] > arr[mid] < arr[right]:
        if n < arr[mid]:
            return search(arr[:mid], n)
        else:
            return search(arr[mid + 1:], n)

    return idx
