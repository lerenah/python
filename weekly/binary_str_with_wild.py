def perms(str):
    rest = []
    perms_helper(str, [], rest)
    return rest

def perms_helper(str, pos=[], rest=[]):
    if len(pos):
        pos = pos
    possibles = ''
    if len(str) == 0:
        rest.append(''.join(pos))
        pos = []
        return possibles
    if str[0] == '?':
        res = pos[:]
        perms_helper('1' + str[1:], pos, rest)
        pos = res
        perms_helper('0' + str[1:], pos, rest)
    else:
        possibles += str[0]
        pos.append(possibles)
        perms_helper(str[1:], pos, rest)


    return possibles
