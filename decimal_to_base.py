hex_conversions = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}


def convert_any_base(n, case):
    num = []
    base = len(case)
    if base == 1:
        return case * n
    negative = False
    if n < 0:
        negative = True
        n = abs(n)
    while n > 0:
        rem = n % base
        if base == 6:
            num.append(str(case[rem]))
        else:
            num.append(str(case[rem - 1]))
        n = n // base
        # use n to get str character
    num = list(reversed(num))
    if negative:
        return '-' + ''.join(num)
    return "".join(num).strip("0")
