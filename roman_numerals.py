conversions = {
        'I': 1,
        'VI': 4,
        'V': 5,
        'XI': 9,
        'X': 10,
        'XL': 40,
        'L': 50,
        'XC': 90,
        'C': 100,
        'CD': 400,
        'D': 500,
        'CM': 900,
        'M': 1000
    }

def int_to_roman(n):
    output = ''
    total = n
    while total > 0:
        s = str(total)
        length = len(s) - 1
        num = s[0] + str(0) * length
        for key, val in conversions.items():
            if int(num) == val:
                output += key
        total -= int(num)
    return total, output


print(int_to_roman(199))
