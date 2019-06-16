def longest(str):
    start = 0
    end = 0
    seen = []
    while start in range(len(str)) and end in range(len(str)):
        if not str[end].isalpha():
            str = str.replace(str[end], '')
        if str[end] not in seen:
            seen.append(str[end])
            end += 1
        else:
            seen.pop(0)
            start += 1

    return end - start
