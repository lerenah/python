# get up, down, left, and right
# get edges
# nested for loop
# check for membership of first letter (if word[idx] in col)
# check to see if neighbors == word[idx + 1]


def exist(self, arr, word):
    """
    :type board: List[List[str]]
    :type word: str
    :rtype: bool
    """
    # make another grid
    grid = [[False] * len(arr[0]) for i in range(len(arr))]

    def get_neighbors(row, col, letter):
        if 0 <= row + 1 < len(arr):
            if arr[row + 1][col] == letter and not grid[row + 1][col]:
                yield row + 1, col
        if 0 <= row - 1 < len(arr):
            if arr[row - 1][col] == letter and not grid[row - 1][col]:
                yield row - 1, col
        if 0 <= col + 1 < len(arr[0]):
            if arr[row][col + 1] == letter and not grid[row][col + 1]:
                yield row, col + 1
        if 0 <= col - 1 < len(arr[0]):
            if arr[row][col - 1] == letter and not grid[row][col - 1]:
                yield row, col - 1

    def search(row, col, i):
        print(row, col, word[i])
        if i == len(word):
            return True
        if i == len(word) - 1:
            return arr[row][col] == word[i]
        if arr[row][col] != word[i]:
            return False
        for neighbors in get_neighbors(row, col, word[i + 1]):
            n_row, n_col = neighbors
            grid[n_row][n_col] = True
            if search(n_row, n_col, i + 1):
                return True
            grid[n_row][n_col] = False

        return False

    for row in range(len(arr)):
        for col in range(len(arr[0])):
            grid[row][col] = True
            if search(row, col, 0):
                return True
            grid[row][col] = False

    return False
