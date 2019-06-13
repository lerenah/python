import re

def difference(a, b):
    pattern = re.compile(r'\W')
    if len(a) == 0 or len(b) == 0:
        return 0
    if len(a) != len(b):
        raise Exception('Strings must be the same length.')
    if re.match(pattern, a) or re.match(pattern, b):
        raise Exception('Strings must only contain alphabet chars.')
    count = 0
    for letter in a:
        if letter not in b:
            count += 1
    return count
