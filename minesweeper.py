'''
Where is the Bomb Function
'''
matrix = [
    [1, 1, 1, 0],
    [0, 1, 0, 1],
    [1, 1, 1, 1],
    [0, 1, 1, 0]
]

def get_distance(row, col, web):
    friends = 0

    copy_col = col
    # walk to the left
    while copy_col >= 0:
        if (copy_col - 1) >= 0:
            if web[row][copy_col - 1] == 0:
                break
            elif web[row][copy_col - 1] == 1:
                friends += 1
        copy_col -= 1

    # walk to the right
    copy_col = col
    while (copy_col + 1) in range(len(web)):
        if copy_col < len(web):
            if web[row][copy_col + 1] == 0:
                break
            elif web[row][copy_col + 1] == 1:
                friends += 1
        copy_col += 1

    # walk up
    copy_row = row
    while copy_row >= 0:
        if (copy_row - 1) >= 0:
            if web[copy_row - 1][col] == 0:
                break
            elif web[copy_row - 1][col] == 1:
                friends += 1
        copy_row -= 1

    # walk down
    copy_row = row
    while (copy_row + 1) in range(len(web)):
        if copy_row < len(web):
            if web[copy_row + 1][col] == 0:
                break
            elif web[copy_row + 1][col] == 1:
                friends += 1
        copy_row += 1

    return friends


'''
Solves MineSweeper game!
'''
def safe_steps(web):
    for idx, val in enumerate(web):
        for index, el in enumerate(val):
            if el != 0:
                web[idx][index] = get_distance(idx, index, web)
    return web

print(safe_steps(matrix))
