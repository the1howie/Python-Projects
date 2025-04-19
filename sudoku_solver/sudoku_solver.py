"""
Credit to Srini Devadas (MIT) for the solver algorithm.
https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-s095-programming-for-the-puzzled-january-iap-2018/

Given a partially filled in Sudoku board, complete the puzzle
obeying the rules of Sudoku via brute force and search.
"""

import os
import copy

# global variable
backtracks = 0


def findNextCellToFill(grid):
    # This procedure finds the next empty square to fill on the Sudoku grid
    for x in range(0, 9):
        for y in range(0, 9):
            if grid[x][y] == 0:
                return x, y
    return -1, -1


def isValid(grid, i, j, e):
    # This procedure checks if setting the (i, j) square to e is valid
    rowOk = all([e != grid[i][x] for x in range(9)])
    if rowOk:
        columnOk = all([e != grid[x][j] for x in range(9)])
        if columnOk:
            # finding the top left x,y co-ordinates of
            # the section or sub-grid containing the i,j cell
            secTopX, secTopY = 3 * (i // 3), 3 * (j // 3)
            for x in range(secTopX, secTopX + 3):
                for y in range(secTopY, secTopY + 3):
                    if grid[x][y] == e:
                        return False
            return True
    return False


def solveSudoku(grid, i=0, j=0):
    # This procedure fills in the missing squares of a Sudoku puzzle
    # obeying the Sudoku rules through brute-force guessing and checking
    global backtracks

    # find the next cell to fill
    i, j = findNextCellToFill(grid)
    if i == -1:
        return True

    for e in range(1, 10):
        # Try different values in i, j location
        if isValid(grid, i, j, e):
            grid[i][j] = e
            if solveSudoku(grid, i, j):
                return True

            # Undo the current cell for backtracking
            backtracks += 1
            grid[i][j] = 0

    return False


def printSudoku(grid):
    # Print grid at command line.
    numrow = 0
    for row in grid:
        if numrow % 3 == 0 and numrow != 0:
            print(" ")
        print(row[0:3], " ", row[3:6], " ", row[6:9])
        numrow += 1
    return


class style:
    # Command line colours
    BLACK = "\033[30m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"
    WHITE = "\033[37m"
    UNDERLINE = "\033[4m"
    RESET = "\033[0m"


def printSudokuColor(grid, orig=None):
    # Print grid at command line in distinguishing colours.
    os.system("")
    for i, row in enumerate(grid):
        if i % 3 == 0 and i != 0:
            print(" ")
        for j, num in enumerate(row):
            s = " " * 3 if (j % 3 == 0 and j != 0) else ""
            if orig is None:
                c = f"{s}{style.CYAN}{num}{style.RESET} " if num != 0 else f"{s}{num} "
            else:
                c = (
                    f"{s}{style.CYAN}{num}{style.RESET} "
                    if num == orig[i][j]
                    else (
                        f"{s}{style.GREEN}{num}{style.RESET} "
                        if num != 0
                        else f"{s}{num} "
                    )
                )
            print(f"{c} ", end="")
        print()
    return


if __name__ == "__main__":
    # Input original grid manually
    o_grid = [
        [0, 1, 0, 0, 0, 8, 0, 0, 6],
        [3, 6, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 5, 0, 0, 0, 0, 7],
        [0, 0, 0, 0, 8, 4, 5, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [9, 0, 5, 0, 1, 3, 8, 0, 0],
        [0, 0, 2, 0, 9, 0, 0, 0, 0],
        [0, 0, 3, 7, 0, 0, 0, 0, 0],
        [7, 0, 0, 0, 0, 0, 4, 0, 0],
    ]

    grid = copy.deepcopy(o_grid)

    backtracks = 0
    print("Sudoku to be solved:")
    printSudokuColor(o_grid)
    print("\nSoution:")
    print(solveSudoku(grid))
    printSudokuColor(grid, orig=o_grid)
    print("Backtracks = ", backtracks)

    # Template grid

    # zeros = [
    #     [0, 0, 0, 0, 0, 0, 0, 0, 0],
    #     [0, 0, 0, 0, 0, 0, 0, 0, 0],
    #     [0, 0, 0, 0, 0, 0, 0, 0, 0],
    #     [0, 0, 0, 0, 0, 0, 0, 0, 0],
    #     [0, 0, 0, 0, 0, 0, 0, 0, 0],
    #     [0, 0, 0, 0, 0, 0, 0, 0, 0],
    #     [0, 0, 0, 0, 0, 0, 0, 0, 0],
    #     [0, 0, 0, 0, 0, 0, 0, 0, 0],
    #     [0, 0, 0, 0, 0, 0, 0, 0, 0],
    # ]
