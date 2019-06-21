str = 'ABCCCBB'

def crush_it(str):
    i = 0
    while i in range(len(str) - 1):
        if str[i] == str[i + 1] and str[i] == str[i + 2]:
            str = str.replace(str[i], '')
            i = 0
            continue
        i += 1
    return str

print(crush_it(str))
