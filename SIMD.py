def simd_average(a, b):
    c = 0
    for i in range(8):
        a2 = ((a << ((7 - i) * 8)) & 0xFFFFFFFFFFFFFFFF) >> 56
        b2 = ((b << ((7 - i) * 8)) & 0xFFFFFFFFFFFFFFFF) >> 56
        c2 = (a2 ^ b2) + ((a2 & b2) << 1)
        c2 >>= 1
        c |= c2 << (8 * i)

    return c


print(hex(simd_average(0x0102030405060708, 0x0807060504030201)))
