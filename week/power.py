def power(x, n):
    num = abs(n)
    if n == 0:
        return 1
    elif n == 1:
        return x
    else:
        while num > 1:
            x *= x
            num -= 1
        return x
