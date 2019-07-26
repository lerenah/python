'''
Given two arrays:



1) arr1 of size n, which contains n positive integers sorted in increasing order.

2) arr2 of size (2*n) (twice the size of first), which contains n positive integers sorted in increasing order in its first half. Second half of this array arr2 is empty. (Empty elements are marked by 0).



Write a function that takes these two arrays, and merges the first one into second one, resulting in an increasingly sorted array of (2*n) positive integers.

'''


def merger_first_into_second(arr1, arr2):
    #
    # Write your code here.
    #
    l_idx = 0
    r_idx = 0
    while l_idx < len(arr1) and r_idx < len(arr2):
        if arr1[l_idx] <= arr2[r_idx]:
            arr2.pop()
            arr2.insert(r_idx, arr1[l_idx])
            l_idx += 1
        else:
            r_idx += 1
    if l_idx < len(arr1):
        if 0 in arr2:
            i = len(arr2) - 1
            while i >= 0:
                if arr2[i] == 0:
                    arr2.pop()
                i -= 1
        arr2.extend(arr1[l_idx:])

    return arr2


print(merger_first_into_second([3, 5, 4, 11], [1, 2, 7, 9, 0, 0, 0, 0]))
