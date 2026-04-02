from math import sqrt


def quadratic_formula(p):
    # formula derived from completing the square
    # for the quadratic f(x) = ax² + bx + c
    # where p is the list of coefficients
    # i.e., p = [a, b, c]
    a, b, c = p
    delta = b**2 - 4 * a * c
    r1 = (-b - sqrt(delta)) / (2 * a)
    r2 = (-b + sqrt(delta)) / (2 * a)
    return [r1, r2]


# e.g. f(x) = 9x² - 12x - 5
# coefficients: a = 9, b = -12, c = -5
p = [9, -12, -5]
r = quadratic_formula(p)

# print roots
print(r)
