import numpy as np
from itertools import combinations


def sum_combinations(n, K):
    # All possible combinations of n numbers,
    # from values 1 to 9 without duplicates,
    # that add up to K.
    x = np.arange(1, 10)
    combos_list = []
    for combo in combinations(x, n):
        if sum(combo) == K:
            combos_list.append(combo)
    return combos_list


def validate_int(num):
    try:
        return int(num)
    except Exception as e:
        raise Exception(e)


def yn_bool(txt):
    txt = txt.strip()
    if len(txt) == 0:
        # default, press Enter
        return True
    elif txt[0].upper() in ["N", "F", "0"]:
        # No or False
        return False
    else:
        # Yes, True or anything else
        return True


def main():
    # number of squares, max 9
    n = validate_int(input("Enter number of squares (max 9): "))
    # sum of the squares, max 45
    K = validate_int(input("What must they add up to (max 45)? "))

    if (n > 0 and n <= 9) and (K > 0 and K <= 45):
        print("\n{} numbers that add up to {}:".format(n, K))
        combos = sum_combinations(n, K)
        if combos != []:
            for combo in combos:
                print(", ".join([f"{x:1d}" for x in combo]))
        else:
            print("No possible combinations.")
    else:
        print("Invalid inputs.")

    carry_on = yn_bool(input("Carry on? (Y/n) "))
    return carry_on


if __name__ == "__main__":
    carry_on = True
    while carry_on:
        carry_on = main()
        print()
    print("Good bye!\n")
