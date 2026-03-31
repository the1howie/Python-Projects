import numpy as np

# e.g. f(x) = 9x² - 12x - 5
# coefficients: a = 9, b = -12, c = -5
p = [9, -12, -5]
r = np.roots(p)

# roots are 5/3 and -1/3
print(r)
