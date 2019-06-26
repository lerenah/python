def combo(arr, n):
    combos = []
    if n == 0:
        return 1
    if len(arr) == 0:
        return 0
    else:
        mixture = []
        if sum(arr) == n:
            combos.append(arr)
        for el in arr:
            target = n - el
            if target in arr and ([el, target] not in combos or [target, el] not in combos):
                combos.append([target, el])
            if n % el != 0:
                continue
            else:
                combos.append([el] * (n // el))
            half = el
            while half <= n // 2:
                mixture.append(el)
                half += el
            if sum(mixture) == n and mixture not in combos:
                combos.append(mixture)
                mixture = []


    return len(combos)
