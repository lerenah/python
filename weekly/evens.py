
'''
You are given an integer array arr, of size n. Group and rearrange them (in-place) into evens and odds in such a way that group of all even integers appears on the left side and group of all odd integers appears on the right side.

'''
def swap(arr, i, j):
  arr[i], arr[j] = arr[j], arr[i]

def evens(arr):
    end = len(arr) - 1
    start = 0
    neg = start

    for pos in range(start + 1, end + 1):
        if arr[pos] % 2 == 0:
            neg += 1
            swap(arr, pos, neg)
    if arr[0] % 2 != 0:
        temp = arr[0]
        arr.remove(arr[0])
        arr.append(temp)

    return arr
