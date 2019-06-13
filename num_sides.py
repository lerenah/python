def all_ones(arr):
    for row in arr:
       if 0 in row:
           return False
       else:
           continue
    return True


def num_sides(board):
    walls = 4
    for i, row in enumerate(board):
        if all_ones(board):
            return 4
        for idx, col in enumerate(row):
            if col == 0 and idx in range(1, len(row) - 1):
                walls += 3
            elif col == 0 and i in range(1, len(board) - 1):
                walls += 3
            elif col == 0 and i == idx:
                walls += 4
            elif col == 0:
                walls += 2

    return walls
