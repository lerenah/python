def longest(str):
    count = 0
    start = 0
    seen = ''
    while start in range(len(str)):
        if not str[start].isalpha():
            start += 1
            continue
        elif str[start] not in seen:
            seen += str[start]
            count += 1
            start += 1
        else:
            start += 1
            continue
    return count
