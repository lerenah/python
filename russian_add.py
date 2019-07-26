def russian(a, b):
    z = 0
    while a > 0:
        # if a is odd, add b to z
        if a % 2 == 1:
            z += b
        # then double b
        b = b << 1
        # then divide a in half
        a = a >> 1
    return z


print(russian(3, 5,))
