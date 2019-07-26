def threeNumberSum(array, targetSum):
    # Write your code here.
    if not len(array):
        return []
    output = []
    n = len(array)
    array.sort()
    for i, num in enumerate(array):
        if num > 0 and array[i] == array[i - 1]:
            continue
        left = i + 1
        right = n - 1
        while left < right:
            s = num + array[left] + array[right]
            if s > targetSum:
                right -= 1
            elif s < targetSum:
                left += 1
            else:
                output.append([num, array[left], array[right]])
                left += 1
                right -= 1

    return output
