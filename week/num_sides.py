def all_ones(arr):
    for row in arr:
       if 0 in row:
           return False
       else:
           continue
    return True

def num_sides(board):
    num_zeros = 0
    for row in board:
        if all_ones(board):
            return 4
        else:
            if len(row) > row.index(0) > 1:
                num_zeros += 4
            else:
                num_zeros += row.count(0)

    walls = 4 + (num_zeros * 2)
    return walls
