

class Board:
    def __init__(self):
        self.grid = [[None for _ in range(14)] for _ in range(12)]

    def objectInSquare(self, x, y):
        return self.grid[y][x]
