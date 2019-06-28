str = 'ABCCCBB'

def crush_it(str):
    i = 0
    while i in range(len(str)) and i + 2 in range(len(str)):
        if str[i] == str[i + 1] and str[i] == str[i + 2]:
            str = str[:i] + str[i + 3:]
            i = 0
            continue
        i += 1
    return str
