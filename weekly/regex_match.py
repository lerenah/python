def reg_match(str1, str2):
    if not len(str1):
        return True
    if str1[0] != str2[0] and str2[0] != '*':
        return False
    elif str2[0] == '*':
        return reg_match(str1[1:], str2[:])
    else:
        return reg_match(str1[1:], str2[1:])


print(reg_match('abcedfase', 'abc*d'))
