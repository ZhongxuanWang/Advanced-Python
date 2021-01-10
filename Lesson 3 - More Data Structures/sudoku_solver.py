import numpy as np

grid = np.array([
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
])


# Helper function
def possible(y, x, n):
    if grid[y][x] != 0 or n in grid[y] or n in grid[:, x]:
        return False
    y0 = (y // 3) * 3  # In some cases, why not try solve arithmetically?
    x0 = (x // 3) * 3
    return n not in grid[y0:y0 + 3, x0:x0 + 3]


def solve():
    global grid
    for y in range(9):
        for x in range(9):
            # if open
            if grid[y][x] == 0:
                for n in range(1, 10):
                    if possible(y, x, n):
                        grid[y][x] = n
                        solve()
                        grid[y][x] = 0  # when encounters dead end
                return
    print(np.matrix(grid))
    input("Next?")


solve()

