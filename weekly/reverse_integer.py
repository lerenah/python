def reverse(self, x):
    """
    :type x: int
    :rtype: int
    """
    sign = -1 if x < 0 else 1
    num = x
    num = -num if sign == -1 else num
    digits = []
    base = 1
    while num / base != 0:
        result = num % 10
        num = float((num - result) / 10)
        base *= 10
        digits.append(result)

    # get number of 0's needed
    base /= 10

    output = 0
    for digit in digits:
        output += (digit * base)
        base /= 10
        if output > 2**31 or output < -2**31:
            return 0
    return int(-output) if sign < 0 else int(output)
