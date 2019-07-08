'''
Assume that the input is an array of size 'n' where 'n' is an even number. Additionally, assume that half the integers are even and the other half are odd. Print only those permutations where odd and even integers alternate, starting with odd.
'''


def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


def even_perms(arr, n):
    if n == len(arr) - 1:
        if arr[1] % 2 == 0 and arr[3] % 2 == 0:
            print(arr)
        return arr
    for j in range(n, len(arr)):
        swap(arr, n, j)
        even_perms(arr, n + 1)
        swap(arr, n, j)


def perms(arr):
    return even_perms(arr, 0)
