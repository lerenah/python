'''
Assume that the input is an array of characters. Print any one permutation that is also a word in the dictionary. Assume that you have two library functions you can use.



bool ValidWord(char array a) returns true if and only if the string a is a dictionary word.
bool ValidWordPrefix(char array a, int a_size) returns true if and only if a[0...a_size-1] is a prefix of at least one word in the dictionary.
'''


import enchant

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

def dict_perms(arr, n):
    if n == len(arr) - 1:
        if enchant.Dict("en_US").check(f'{arr}'):
            print(arr)
        return arr
    for j in range(n, len(arr)):
        swap(arr, n, j)
        dict_perms(arr, n + 1)
        swap(arr, n, j)


def perms(arr):
    return dict_perms(arr, 0)
