grid = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]]


# For user input in console


# w = 9
# h = 9
# grid = [[0] * w for i in range(h)]
#
#
# print("Please enter the numbers (Any blank space is represented with a zero)")
#
#
# for y in range(9):
#     for x in range(9):
#        grid[y][x] = input()


# Checks for the three parameters that a number needs in a sudoku puzzle
def test(y, x, z):
    global grid
    for a in range(0, 9):
        if grid[y][a] == z:
            return False
    for b in range(0, 9):
        if grid[b][x] == z:
            return False
    x0 = (x // 3) * 3
    y0 = (y // 3) * 3
    for c in range(0, 3):
        for d in range(0, 3):
            if grid[y0 + c][x0 + d] == z:
                return False
    return True


# Uses test() and recursion to find compatible numbers
def solve():
    global grid
    for y in range(9):
        for x in range(9):
            if grid[y][x] == 0:
                for n in range(1, 10):
                    if test(y, x, n):
                        grid[y][x] = n
                        solve()
                        grid[y][x] = 0
                return
    print()
    for i in range(9):
        temp = ''
        for j in range(9):
            temp += str(grid[i][j]) + "  "

        print(temp)


# Runs the program
solve()
