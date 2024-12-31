# https://mathworld.wolfram.com/MagicSquare.html
# https://uk.mathworks.com/help/matlab/ref/magic.html

import numpy as np

def magic(n):
    """Simulating MATLAB's magic() function """
    if n < 3:
        return None
    elif n % 2 != 0:
        return siamese(n)
    elif n % 4 == 0:
        return diagonals(n)
    else:
        return lux(n)

def siamese(n):
    """Odd square, de la Loubre's - Siamese method """
    square = np.zeros((n, n), dtype=int)
    r, c, x = 0, n // 2, 1
    square[r, c] = x
    x += 1
    r = (r - 1) % n
    c = (c + 1) % n
    while x <= n**2:
        if square[r, c] != 0:
            r = (r + 2) % n
            c = (c - 1) % n
        square[r, c] = x
        x += 1
        r = (r - 1) % n
        c = (c + 1) % n
    return square

def diagonals(n):
    """Doubly even square, cross-off diagonals """
    square = np.reshape(np.arange(1, n**2 + 1), (n, n))
    for r4 in range(n // 4):
        for c4 in range(n // 4):
            # split the n-by-n square into 4-by-4 squares
            for r in range(r4 * 4, (r4 + 1) * 4):
                for c in range(c4 * 4, (c4 + 1) * 4):
                    # cross-off diagonals
                    if (r % 4) == (c % 4):
                        square[r, c] = (n**2 + 1) - square[r, c]
                        square[r, n - c - 1] = (n**2 + 1) - square[r, n - c - 1]
    return square

def lux_config(m):
    """set up the LUX instructions matrix """
    l = 2 * m + 1
    lux_sq = np.zeros((l, l), dtype='S1')
    for r in range(m + 1):
        for c in range(l):
            lux_sq[r, c] = 'L'
    for c in range(l):
        lux_sq[m + 1, c] = 'U'
    lux_sq[m, m], lux_sq[m + 1, m] = lux_sq[m + 1, m], lux_sq[m, m]
    if m - 1 > 0:
        for r in range(m + 2, l):
            for c in range(l):
                lux_sq[r, c] = 'X'
    return lux_sq

def lux(n):
    """Singly even square, LUX method 
       -- This method differs to MATLAB
    """
    square = np.zeros((n, n), dtype=int)
    m = (n - 2) // 4
    l = 2 * m + 1
    lux_sq = lux_config(m)

    # define the LUX shapes
    def L_shape(four_nums, loc):
        nonlocal square
        r0, c0 = loc
        square[r0, c0 + 1] = four_nums[0]
        square[r0 + 1, c0] = four_nums[1]
        square[r0 + 1, c0 + 1] = four_nums[2]
        square[r0, c0] = four_nums[3]
    
    def U_shape(four_nums, loc):
        nonlocal square
        r0, c0 = loc
        square[r0, c0] = four_nums[0]
        square[r0 + 1, c0] = four_nums[1]
        square[r0 + 1, c0 + 1] = four_nums[2]
        square[r0, c0 + 1] = four_nums[3]
    
    def X_shape(four_nums, loc):
        nonlocal square
        r0, c0 = loc
        square[r0, c0] = four_nums[0]
        square[r0 + 1, c0 + 1] = four_nums[1]
        square[r0 + 1, c0] = four_nums[2]
        square[r0, c0 + 1] = four_nums[3]
    
    def fill_shape(shape, four_nums, loc):
        match shape:
            case 'L':
                L_shape(four_nums, loc)
            case 'U':
                U_shape(four_nums, loc)
            case 'X':
                X_shape(four_nums, loc)
    
    # next, use the Siamese method for 2-by-2 squares
    r, c = 0, m
    x = 1
    vals = np.arange(x, x + 4)
    shape = lux_sq[r, c].decode("utf-8")
    fill_shape(shape, vals, (r * 2, c * 2))

    x += 4
    vals = np.arange(x, x + 4)
    r = (r - 1) % l
    c = (c + 1) % l
    while vals[-1] <= n**2:
        if sum(square[r*2:r*2+1, c*2:c*2+1]) != 0:
            r = (r + 2) % l
            c = (c - 1) % l
        shape = lux_sq[r, c].decode("utf-8")
        fill_shape(shape, vals, (r * 2, c * 2))
        x += 4
        vals = np.arange(x, x + 4)
        r = (r - 1) % l
        c = (c + 1) % l
    return square

def magic_constant(n):
    """Calculate the Magic Constant """
    return n * (n**2 + 1) // 2

def validate(square):
    """Validate a magic square """
    valid_square = True
    error_messages = []

    # get 2d array dimensions
    if isinstance(square, np.ndarray):
        square = np.array(square)
    n, m = square.shape
    if n != m:
        return (False, ["Not a square matrix."])
    
    # get the magic constant as k
    k = magic_constant(n)

    # validation subroutine
    def check_k(vector, vector_name):
        nonlocal k
        nonlocal valid_square
        nonlocal error_messages
        # the actual sum check
        sum_check = sum(vector) == k
        valid_square = valid_square and sum_check
        if not sum_check:
            error_messages.append("{} does not add up to {}".format(vector_name, k))
    
    # validate row sums
    for r in range(n):
        check_k(square[r, :], "Row " + str(r + 1))
    
    # validate column sums
    for c in range(n):
        check_k(square[:, c], "Column " + str(r + 1))
    
    # validate diagonal sums
    check_k(square.diagonal(), "Main diagonal")
    check_k(square[:, ::-1].diagonal(), "Perpendicular diagonal")

    return (valid_square, error_messages)
