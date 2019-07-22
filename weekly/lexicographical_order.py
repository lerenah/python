'''You are given a string array named arr, of size N, containing KEYS and VALUES separated by a space.


Your task is to find, for each unique KEY, the number of VALUES with that key and the VALUE with the highest lexicographical order (also called alphabetical order OR dictionary order).


(Have a look at the sample test cases for more clarity.)'''


def solve(arr):
    #
    # Write your code here.
    #
    output = []
    arr_dict = {}
    for el in arr:
        idx = el.index(' ')
        key = el[:idx]
        val = el[idx + 1:]
        arr_dict.setdefault(key, []).append(val)

    for key, val in arr_dict.items():
        output.append(f'{key}:{len(val)},{max(val)}')

    return output
