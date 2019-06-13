def power(x, n):
    num = abs(n)
    if x == 0:
        return x
    if n == 0 and x > 0:
        return 1
    elif n == 1:
        return x
    else:
        base = x
        if n < 0:
            while n < 1:
                base /= x
                n += 1

        else:
            while num > 1:
                base *= x
                num -= 1
    return base
