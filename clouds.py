def find_neighbors(grid, row, col):
    if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]) or grid[row][col] == 0:
        return 0
    grid[row][col] = 0
    find_neighbors(grid, row + 1, col)
    find_neighbors(grid, row - 1, col)
    find_neighbors(grid, row, col - 1)
    find_neighbors(grid, row, col + 1)
    return 1


def adjacent(clouds):
    num_clouds = 0
    for i, row in enumerate(clouds):
      if 1 in row:
        for j, col in enumerate(row):
            if col == 1:
                num_clouds += find_neighbors(clouds, i, j)
    return num_clouds
