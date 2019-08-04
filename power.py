def myPow(self, x, n):
    """
    :type x: float
    :type n: int
    :rtype: float
    """
    exp = abs(n)
    output = 1
    while exp > 0:
        output *= x
        exp -= 1
    if n < 0:
        return 1 / output

    return output
