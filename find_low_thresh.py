def find_lowest(arr, target):
    if sum(arr) == target:
        lowest = max(arr)
    elif sum(arr) < target:
        raise Exception('Target must be smaller.')
    elif len(arr) == target:
        return 1
    else:
        new_arr = []
        while sum(arr) > target:
            _min = min(arr)
            new_arr.append(_min)
            arr.remove(_min)

        total = sum(new_arr)
        left_over = target - total
        lowest = left_over / len(arr)
        for el in arr:
            new_arr.append(lowest)


    return lowest
