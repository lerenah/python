def crush_it(str):
    i = 0
    j = i + 1
    while i in range(len(str)) and j + 1 in range(len(str)):
        if str[i] == str[j] and str[j] == str[j + 1]:
            start = i
            while str[i] == str[j]:
                i += 1
                j += 1
            str = str[:start] + str[j:]
            i = 0
            j = i + 1
            continue
        i += 1
        j += 1
    return str
