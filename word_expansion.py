def expansion(str):
    scale = 0
    contents = ''
    start_idx = str.index('[') - 1
    stop_idx = str.index(']')
    str_to_int = int(str[start_idx])
    if type(str_to_int) == int:
        while scale in range(str_to_int):
            contents += str[start_idx + 2:stop_idx]
            scale += 1
    return contents

print(expansion('3[a]'))
