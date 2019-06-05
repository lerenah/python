# get up, down, left, and right
# get edges
# nested for loop
# check for membership of first letter (if word[idx] in col)
# check to see if neighbors == word[idx + 1]

def get_neighbors(idx, index, letter, arr):
    if (idx + 1) in range(len(arr)):
        if arr[idx + 1][index] == letter:
            print(letter)
            return idx + 1, index
    if (idx - 1) in range(len(arr)):
        if arr[idx - 1][index] == letter:
            print(letter)
            return idx - 1, index
    if (index - 1) in range(len(arr[0])):
        if arr[idx][index - 1] == letter:
            print(letter)
            return idx, index - 1
    if (index + 1) in range(len(arr[0])):
        if arr[idx][index + 1] == letter:
            print(letter)
            return idx, index + 1

    else:
        print('False')
        return -1, -1


def word_find(arr, str):
    count = 0
    for idx, row in enumerate(arr):
        if str[count] in row:
            for index, col in enumerate(row):
                if col in str and col == str[count]:
                    letter = str[count + 1]
                    if not get_neighbors(idx, index, letter, arr):
                        continue
                    else:
                        print(str[count])
                        mod_idx, mod_index = get_neighbors(idx, index, letter, arr)
                        reset = count
                        count += 1
                        while (mod_idx and mod_index) and len(str) - 1 >= count:
                            mod_idx, mod_index = get_neighbors(mod_idx, mod_index, str[count+1], arr)
                            if mod_idx == -1 and mod_index == -1:
                                count = reset
                                break
                            elif count == len(str) - 1:
                                return True
                            else:
                                count  += 1



