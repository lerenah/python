def smallest_subarray_with_given_sum(s, arr):
    # TODO: Write your code here
    # [3, 4, 1, 1, 6], S=8
    res = 0
    end, start = 0, 0  # 5, 1
    length = float('inf')  # 3
    temp_sum = 0  # 12
    while end in range(len(arr)):
        # if (end - start) + 1 >= length:
        #   start += 1
        temp_sum += arr[end]
        if temp_sum >= s:
            if (end - start) + 1 < length:  # 2 - 0 = 3
                length = (end - start) + 1
                temp_sum -= arr[start]
                temp_sum -= arr[end]
                start += 1
                end -= 1
        end += 1

    return length


# alternative
def smallest_subarray_with_given_sum(s, arr):
    temp_sum = 0
    length = math.inf
    end, start = 0, 0

    for end in range(len(arr)):
        temp_sum += arr[end]  # add the next element
        # shrink the window as small as possible until the 'window_sum' is smaller than 's'
        while temp_sum >= s:
            length = min(length, end - start + 1)
            temp_sum -= arr[start]
            start += 1
    if length == math.inf:
        return 0
    return length
