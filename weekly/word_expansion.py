def word(str):
    nums = '123456789'
    output = ''
    i = 0
    idx = 0
    q = []
    scale = []
    start = False
    while idx in range(len(str)):
        if str[idx] == '[':
            start = True
            idx += 1
            continue
        if str[idx] == ']':
            num = int(''.join(scale))
            output += ''.join(q) * num
            idx += 1
            # reset everything
            start = False
            scale = []
            q = []
            continue
        if str[idx] in nums and start:
            i = idx
            while str[i] != ']':
                i += 1
            q.extend(word(str[idx:i + 1]))
            idx = i + 1
            continue
        if start:
            q.append(str[idx])
            idx += 1
            continue
        elif str[idx] in nums:
            scale.append(str[idx])
            idx += 1
            continue
        else:
            output += str[idx]
            idx += 1

    return output

    # optimal solution
    def decodeString(s):
        """
        :type s: str
        :rtype: str
        """
        words = []
        scale = []
        num = ''
        output = ''

        for el in s:
            if el.isdigit():
                num += el
            elif el.isalpha():
                output += el
            elif el == '[':
                words.append(output)
                scale.append(int(num))
                num, output = '', ''
            elif el == ']':
                output = words.pop() + output * scale.pop()

        return output

