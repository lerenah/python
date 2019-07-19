def busy_schedule(arr):
    sort_arr = sorted(arr)
    merged = [sort_arr[0]]
    for start, end in sort_arr[1:]:
        prev_start, prev_end = merged[-1]
        if prev_end >= start:
            if end >= prev_end:
                merged[-1] = (prev_start, end)
        else:
            merged.append((start, end))

    return merged
