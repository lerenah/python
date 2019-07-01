hex_conversions = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}

def convert_any_base(n, base):
    num = []
    negative = False
    if n < 0:
        negative = True
        n = abs(n)
    if base == "0123456789ABCDEF":
        base = 16
    elif base == "01":
        base = 2
    elif base == "QWERTY":
        base = 6
    while n > 0:
        rem = n % base
        if rem > 9 and base == 16:
            num.append(hex_conversions[rem])
        else:
            num.append(str(rem))
        n = n // base
    num = list(reversed(num))
    if negative:
        return '-' + ''.join(num)
    return "".join(num)
