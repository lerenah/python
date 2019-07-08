'''
Given an integer array arr of size N, find all magical triplets in it.

Magical triplet is the group of 3 integers, whose sum is zero.

Note that magical triplets may or may not be made of consecutive numbers in arr.

Input/Output Format For The Function:

Input Format:


There is only one argument: integer array arr.



Output Format:



Return a string array res.

Each string in res array corresponds to a magical triplet in arr.

Note that:

Order of strings(magical triplets) in res does not matter.
Order of elements inside a magical triplet does not matter. i.e. if your output triplet have same elements, but only in different order, then it's an acceptable triplet and will lead to an acceptable solution.
There should be no duplicate triplets in res. Eg: 1,1,-2 and 1,-2,1 are duplicates.
If no such triplets are found, then return an empty array as res.
'''


def findZeroSum(arr):
    if not arr or len(arr) < 3:
        return []
    res = []
    arr.sort()
    for idx, el in enumerate(arr[:-2]):
        if idx > 0 and arr[idx] == arr[idx - 1]:
            continue
        i = idx + 1
        j = len(arr) - 1
        while i < j:
            zero = el + arr[i] + arr[j]
            if zero > 0:
                j -= 1
            elif zero < 0:
                i += 1
            else:
                res.append(f'{el},{arr[i]},{arr[j]}')
                while i + 1 < j and arr[i] == arr[i + 1]:
                    i += 1
                while j - 1 > i and arr[j] == arr[j - 1]:
                    j -= 1
                i += 1
                j -= 1

    return res
