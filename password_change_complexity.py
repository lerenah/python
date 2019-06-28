def routine_check(str1, str2):
    count = 0
    for char in str1:
        if char not in str2:
            count += 1
    return count

print(routine_check('xxxx', 'yyyy'))
