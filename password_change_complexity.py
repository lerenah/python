def routine_check(str1, str2):
    count = 0
    diff = 0
    last_letter = ''
    for char in str1:
        if char not in last_letter:
            count = str1.count(char)
            num = str2.count(char)
            diff += count - num
        last_letter += char

    return diff
