def compress(data):
    compressor = {}
    for datum in data:
        if datum not in compressor:
            compressor[datum] = 1
        else:
            compressor[datum] += 1
    return compressor


def decompress(obj):
    str = ''
    for key, val in obj.items():
        for i in range(val):
            str += key
    return str
