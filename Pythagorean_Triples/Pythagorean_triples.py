"""
Formula for generating Primitive Pythagorean Triples
---------------------------------------------------------------------------------
INPUTS: The number of gradients 'm' is the input to this program.

The 'formula' is achieved by solving a system of two equations:
x^2 + y^2 = 1
y = mx + m, where m must be rational.

Solutions to this non-linear systems are:
(-1, 0) - This is the point that the line must pass throught.
((1-m^2)/(1+m^2), 2m/(1-m^2)(1+m^2)) - The x and y coordinate provide us with a
'formula' for generting Pythagorean triples.

Conditions: m = k/n where k, n are positive integers with k < n AND gcd(k,n) = 1.

The program generates nCr(n, 2) combinations of Pythagorean triples based on n.
These combinations are then filters by the conditions above.

Inspired by Polar Pi's great video: https://www.youtube.com/watch?v=y718ckf336c
"""

import os
import csv
from typing import List, Set
from operator import itemgetter
from fractions import Fraction
from math import comb


def generate_gradients(count: int = 10) -> Set:
    # rational gradient m
    gradients_list = []

    # the two nested for loops should create nCr(count, 2) number of fractions.
    # For the gradient to be rational we need: numerator < denominator.
    for numerator in range(1, count):
        for denominator in range(numerator + 1, count + 1):
            # Fraction() object actually simplifies the rational fraction,
            # ensuring that the GCD(numerator, denominator) == 1.
            gradients_list.append(Fraction(numerator, denominator))

    # create a set of gradients, which drops the duplicate fractions.
    return set(gradients_list)


def extract_triple(m: Fraction) -> List:
    # solving the system of equations we have:
    # x = a / c = (1 - m^2) /(1 + m^2)
    # y = b / c = (2m) / (1 + m^2)
    # where c is the hypothenuse
    # a and b are the short sides of the right-angle triangle
    a0 = 2 * m
    b0 = 1 - m**2
    c0 = 1 + m**2

    x = Fraction(a0, c0)
    y = Fraction(b0, c0)
    a, c = x.as_integer_ratio()
    b = y.numerator

    return sorted([a, b, c])


def generate_triples(gradients: Set) -> List:
    triples = []
    for m in gradients:
        triples.append(extract_triple(m))
        # print(triples[-1])
    return triples


def filter_duplicate_triples(triples: List) -> List:
    # having unique gradients does not guarantee unique triples.

    # convert the triples into strings which are hasheable
    duplicates = []
    for triple in triples:
        duplicates.append("_".join([str(t) for t in triple]))

    # set guarantees unique values
    triples_set = set(duplicates)

    # convert the strings back to lists of integers
    filtered_triples = []
    for triple in triples_set:
        filtered_triples.append([int(ch) for ch in triple.split("_")])

    return filtered_triples


def get_int_input(prompt: str = "Enter a number: ", lbound: int = 1) -> int:
    # input validation
    x = input(prompt)
    try:
        x = int(x)
    except ValueError:
        try:
            x = int(eval(x))
        except Exception as e:
            raise Exception(e)
    return x if x > lbound else None


def clear_console():
    os.system("cls" if os.name == "nt" else "clear")


def main():
    n = get_int_input("Enter the number of gradients: ")
    if n is None:
        raise ValueError("Invalid input.")
    clear_console()

    gradients = generate_gradients(n)
    triples = generate_triples(gradients)
    pythag_triples = sorted(filter_duplicate_triples(triples), key=itemgetter(0))

    print(
        f"{len(pythag_triples)} Pythagorean Triples out of {comb(n, 2)} combinations:\n"
    )

    # write the output to a file as it is difficult to search the terminal
    with open("pythagorean_triples.csv", "w", newline="") as f:
        writer = csv.writer(f)
        for triple in pythag_triples:
            print(triple)
            writer.writerow(triple)


if __name__ == "__main__":
    clear_console()
    main()
