"""
This spreadsheet uses xlwings Lite (https://lite.xlwings.org/).

Select the script that you would like to run i.e.,
    - sudoky_solver, after inputing grid manually,
    - clear_grid, when you want to start with a blank grid.
"""

import copy
import xlwings as xw
from xlwings import func, script, constants

BACKTRACKS = 0
COLOR_BLACK = "#000000"
COLOR_LIME_GREEN = "#00B612"
COLOR_NEON_GREEN = "#39FF14"
COLOR_DARK_GREEN = "#005708"


@script
def sudoku_solver(book: xw.Book):
    # the main code
    global BACKTRACKS
    BACKTRACKS = 0
    grid_range = book.sheets[0].range("sudoku_grid")
    original_grid = validate_input(grid_range.value)
    grid = copy.deepcopy(original_grid)

    solver(grid)
    print(f"back tracks: {BACKTRACKS}")
    grid_range.value = grid
    format_original(grid_range, original_grid)


@script
def clear_grid(book: xw.Book):
    grid_range = book.sheets[0].range("sudoku_grid")
    grid_range.clear_contents()
    grid_range.color = COLOR_BLACK
    # reformat_range(grid_range)


# -- sudoku solver algorithm --

# Credit to Srini Devadas (MIT) for the solver algorithm.
# https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-s095-programming-for-the-puzzled-january-iap-2018/


def solver(grid, i=0, j=0):
    # This procedure fills in the missing squares of a Sudoku puzzle
    # obeying the Sudoku rules through brute-force guessing and checking
    global BACKTRACKS

    # find the next cell to fill
    i, j = findNextCellToFill(grid)
    if i == -1:
        return True

    for e in range(1, 10):
        # Try different values in i, j location
        if isValid(grid, i, j, e):
            grid[i][j] = e
            if solver(grid, i, j):
                return True

            # Undo the current cell for backtracking
            BACKTRACKS += 1
            grid[i][j] = 0

    return False


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


# -- utils --


def get_shape(grid):
    # return the shape of a 2D list
    try:
        return (len(grid), len(list(zip(*grid))))
    except Exception as e:
        print(e)
        return (len(grid), None)


def validate_input(grid):
    # validate the spreadsheet input
    temp = copy.deepcopy(grid)
    shape = get_shape(temp)
    if shape != (9, 9):
        raise ValueError("Expected 9-by-9 grid.")

    for row in range(shape[0]):
        for col in range(shape[1]):
            if temp[row][col] is None:
                temp[row][col] = 0
            elif not isinstance(temp[row][col], int):
                raise ValueError("Input must be an integer.")
            elif temp[row][col] < 0 or temp[row][col] > 9:
                raise ValueError("Input must be between 1 and 9.")

    return temp


def reformat_range(rng: xw.Range):
    # doesn't work yet.
    for cel in rng:
        cel.font.size = 36
        cel.font.color = COLOR_NEON_GREEN
        cel.font.name = "Consolas"
        # cel.row_height = 46.5
        # cel.column_width = 8.09
        # draw_border(cel)


def format_original(grid_range, original_grid):
    # shade in the original inputs to distinguish them from the solution
    shape = get_shape(original_grid)
    if shape[0] != grid_range.rows.count or shape[1] != grid_range.columns.count:
        raise ValueError("Original grid and output range not the same shape.")

    for row in range(shape[0]):
        for col in range(shape[1]):
            # shade in the original inputs
            if grid_range[row, col].value == original_grid[row][col]:
                grid_range[row, col].color = COLOR_DARK_GREEN


# def draw_border(rng, weight=0):
#     edge_indices = [
#         constants.BordersIndex.xlEdgeTop,
#         constants.BordersIndex.xlEdgeRight,
#         constants.BordersIndex.xlEdgeBottom,
#         constants.BordersIndex.xlEdgeLeft
#     ]

#     if weight==0:
#         rng_weight=constants.BorderWeight.xlThin
#     else:
#         rng_weight=constants.BorderWeight.xlThick

#     # AttributeError: 'Range' object has no attribute 'Borders'

#     for edge_idx in edge_indices:
#         rng.Borders(edge_idx).LineStyle = constants.LineStyle.xlContinuous
#         rng.Borders(edge_idx).Color = COLOR_NEON_GREEN
#         rng.Borders(edge_idx).TintAndShade= 0
#         rng.Borders(edge_idx).Weight = rng_weight
