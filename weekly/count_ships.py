grid = [
    [0, 0, 0, 0],
    [0, "X", 0, 0],
    [0, 0, "X", 0],
    [0, 0, 0, 0],
]

class Ships(object):

    def __init__(self):
        self.grid = grid
        self.ships = False
        self.count = 0
        self.coords = {}
        self.x_coords = []

    def set_coords(self, val, x, y):
        self.grid[x][y] = val
        self.coords[val] = (x, y)

    def get_coords(self, val):
        return self.coords[val]

    def check_for_x(self):
        for x, row in enumerate(self.grid):
            for y, col in enumerate(row):
                if col == 'X':
                    if (x, y) not in self.x_coords:
                        self.x_coords.append((x, y))

    def countShips(self, val1, val2):
        num_ships = 0
        x1, y1 = self.coords[val1]
        x2, y2 = self.coords[val2]
        self.check_for_x()
        for val in self.x_coords:
            if (x1 <= val[0] <= x2) and (y1 < val[1] < y2):
                num_ships += 1
        return num_ships

    def hasShips(self, val1, val2):
        return self.countShips(val1, val2) > 0
