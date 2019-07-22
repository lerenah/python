def find_missing_num(arr):
    missing_num = 0
    highest = max(arr)
    seq_total = (highest * (highest + 1)) // 2
    current_total = sum(arr)
    if seq_total > current_total:
        missing_num = seq_total - current_total
    else:
        missing_num = highest + 1
    return missing_num
