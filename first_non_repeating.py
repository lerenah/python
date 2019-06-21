def first_unique(str):
    char = ''
    left = 0
    right = 1
    while right in range(len(str)):
        if str[left] != str[right]:
            if not len(char):
                char += str[left]
            right += 1
        else:
            char = ''
            left += 1

    return char
