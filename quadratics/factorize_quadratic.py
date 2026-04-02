import os
from math import sqrt, gcd
import cmath as cm


def discriminant(p):
    a, b, c = p
    return b**2 - 4 * a * c


def quadratic_formula(p):
    a, b, _ = p
    delta = discriminant(p)
    try:
        r1 = (-b - sqrt(delta)) / (2 * a)
        r2 = (-b + sqrt(delta)) / (2 * a)
    except ValueError:
        r1 = (-b - cm.sqrt(delta)) / (2 * a)
        r2 = (-b + cm.sqrt(delta)) / (2 * a)
    return [r1, r2]


def int_factorize(p):
    a, b, _ = p
    delta = discriminant(p)
    if delta < 0 or not is_perfect_square(delta):
        raise Exception(
            "Discriminant is not a positive perfect square. Cannot integer factorize."
        )
    rho = abs(int(sqrt(delta)))
    gamma = gcd(2 * a, b - rho)
    zeta = gcd(2 * a, b + rho)
    c1 = 2 * a // gamma
    c2 = (b - rho) // gamma
    c3 = 2 * a // zeta
    c4 = (b + rho) // zeta
    return [c1, c2, c3, c4]


def is_perfect_square(num):
    return sqrt(num) == int(sqrt(num))


def quadratic_expression(a, b, c):
    output = ""
    if abs(a) == 1:
        if a == 1:
            output += "x²"
        else:
            output += "- x²"
    else:
        if a > 0:
            output += str(a) + "x²"
        elif a < 0:
            output += "- " + str(abs(a)) + "x²"
    if b < 0:
        if b == -1:
            output += " - x"
        else:
            output += " - " + str(abs(b)) + "x"
    elif b > 0:
        if b == 1:
            output += " + x"
        else:
            output += " + " + str(b) + "x"
    if c < 0:
        output += " - " + str(abs(c))
    elif c > 0:
        output += " + " + str(c)
    return output


def build_quadratic_factorization(c1, c2, c3, c4):
    output = "("
    if abs(c1) == 1:
        if c1 == -1:
            output += "- x"
        else:
            output += "x"
    else:
        if c1 < 0:
            output += " - " + str(abs(c1)) + "x"
        else:
            output += str(c1) + "x"
    if c2.imag == 0:
        if c2 < 0:
            output += " - " + str(abs(c2)) + ")("
        else:
            output += " + " + str(c2) + ")("
    else:
        output += " + " + str(c2) + ")("
    if abs(c3) == 1:
        if c3 == -1:
            output += "- x"
        else:
            output += "x"
    else:
        output += str(c3) + "x"
    if c4.imag == 0:
        if c4 < 0:
            output += " - " + str(abs(c4)) + ")"
        else:
            output += " + " + str(c4) + ")"
    else:
        output += " + " + str(c4) + ")"
    return output


def get_int(prompt="Enter integer: "):
    ans = input(prompt)
    try:
        return int(ans)
    except ValueError as e:
        raise ValueError(e)


def get_inputs():
    os.system("cls" if os.name == "nt" else "clear")
    print("Enter coefficients a, b & c for quadratic: ax² + bx + c")
    a = 0
    while a == 0:
        a = get_int("Enter coefficient a (NB! a≠0): ")
    b = get_int("Enter coefficient b: ")
    c = get_int("Enter coefficient c: ")
    return [a, b, c]


def main():
    p = get_inputs()
    delta = discriminant(p)
    if delta < 0 or not is_perfect_square(delta):
        r = quadratic_formula(p)
        coef = [1, -1 * r[0], 1, -1 * r[1]]
    else:
        coef = int_factorize(p)

    a, b, c = p
    c1, c2, c3, c4 = coef
    lhs = quadratic_expression(a, b, c)
    rhs = build_quadratic_factorization(c1, c2, c3, c4)
    print("\nQuadratic factorization:\n")
    print(lhs + " = " + rhs + "\n")


if __name__ == "__main__":
    main()
