'''
A disorganized carpenter has a mixed pile of bolts and nuts and would like to find the corresponding pairs of bolts and nuts. Each nut matches exactly one bolt and vice versa. By trying to match a bolt and a nut, the carpenter can see which one is bigger, but she cannot compare two bolts or two nuts directly. Can you help the carpenter match the nuts and bolts quickly?



In other words: You are given a collection of N nuts of different size and N corresponding bolts. You can choose to compare any nut & any bolt to determine whether the nut is larger than the bolt, smaller than the bolt or matches the bolt exactly. However, there is no way to compare two nuts together or two bolts together. (i.e. you cannot sort all nuts or sort all bolts). Write an algorithm to match each bolt to its matching nut.



Note that:

No two nuts are of same size. Similarly, no two bolts are of same size.
A given nut uniquely matches a bolt. i.e. There are no extra unmatched nuts or extra bolts. Every nut has one and only one matching bolt and vice-versa.
'''

import random

nuts = [4, 32, 5, 7]
bolts = [32, 7, 4, 5]


def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


def find_pivot(arr, start, end):
    k = random.randint(start, end)
    pivot = arr[k]

    return pivot, k


def arrange(arr, start, end):
    if start >= end:
        return arr
    smaller = start
    bigger = start
    pivot, idx = find_pivot(arr, start, end)
    swap(arr, start, idx)
    for bigger in range(start + 1, end + 1):
        if arr[bigger] < pivot:
            smaller += 1
            swap(arr, bigger, smaller)
    swap(arr, start, smaller)
    arrange(arr, start, smaller - 1)
    arrange(arr, smaller + 1, end)
    return arr


def solve1(nuts, bolts):
    res = []
    arrange(nuts, 0, len(nuts) - 1)
    arrange(bolts, 0, len(bolts) - 1)
    for idx, el in enumerate(nuts):
        res.append(f'{el} {bolts[idx]}')

    return res
