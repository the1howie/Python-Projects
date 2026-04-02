from sympy import *
from pprint import pprint

x, y = symbols("x y")
init_printing(use_unicode=True)

# e.g. f(x) = 9x² - 12x - 5
y = 9 * x**2 - 12 * x - 5
r = solve(y, x)

# roots of f(x) are:
pprint(r)
