from copy import copy
import random

w = 10
h = 10
grid = [[0] * w for i in range(h)]
grid2 = copy(grid)
counter = 0

for i in range(9):
    for j in range(9):
        grid[i][j] = int(random.random() * 2)

for i in range(9):
    temp = ''
    for j in range(9):
        temp += str(grid[i][j]) + "  "

    print(temp)


def count():
    global grid
    global grid2
    global w
    global h
    global counter
    while True:
        for y in range(h):
            for x in range(w):
                counter = 0
                if x < w + 1:
                    if grid[y][x + 1] == 1:
                        counter += 1
                if x > 1:
                    if grid[y][x - 1] == 1:
                        counter += 1
                if y < h + 1:
                    if grid[y + 1][x] == 1:
                        counter += 1
                if y > 1:
                    if grid[y - 1][x] == 1:
                        counter += 1
                if y < h + 1 and x < w + 1:
                    if grid[y + 1][x + 1] == 1:
                        counter += 1
                if y > 1 and x > 1:
                    if grid[y - 1][x - 1] == 1:
                        counter += 1
                if y < h + 1 and x > 1:
                    if grid[y + 1][x - 1] == 1:
                        counter += 1
                if y > 1 and x < w + 1:
                    if grid[y - 1][x + 1] == 1:
                        counter += 1

                if counter < 2:
                    grid2[y][x] = 0
                elif counter > 3:
                    grid2[y][x] = 0
                elif counter == 3:
                    grid2[y][x] = 1

        grid = grid2
        print()
        for i in range(h):
            temp = ''
            for j in range(w):
                temp += str(grid[i][j]) + "  "

            print(temp)


count()
