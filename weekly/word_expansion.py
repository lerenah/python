def expansion(str):
    scale = 0
    nums = '123456789'
    start = False
    output = ''
    for idx, el in enumerate(str):
        if el == '[':
            start = True
            continue
        elif el in nums and scale == 0:
            scale = int(el)
            continue
        if start and scale > 0:
            while scale > 0:
                index = idx
                while str[index] != ']':
                    if str[index] in nums:
                        output += expansion(str[index:])
                        break
                    else:
                        output += str[index]
                    index += 1
                scale -= 1

            return output
