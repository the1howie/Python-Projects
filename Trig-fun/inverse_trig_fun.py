# Graphs in desmos:
# sin - https://www.desmos.com/calculator/goceqzgbfk
# cos - https://www.desmos.com/calculator/n6m9gmux4z
# tan - https://www.desmos.com/calculator/u4i8pxznbv

from math import *


def round_sig_fig(x, sig_fig=1):
    return round(x, sig_fig - int(floor(log10(abs(x)))) - 1) if x != 0 else 0


def append_solution(
    solutions, angle, lower_bound, upper_bound, bound_incl, sig_fig=None
):
    if angle not in solutions:
        if bound_incl:
            if angle >= lower_bound and angle <= upper_bound:
                solutions.append(
                    angle
                    if sig_fig is None
                    else round_sig_fig(angle, abs(int(sig_fig)))
                )
        else:
            if angle > lower_bound and angle < upper_bound:
                solutions.append(
                    angle
                    if sig_fig is None
                    else round_sig_fig(angle, abs(int(sig_fig)))
                )


def append_right(
    solutions, angle, period, lower_bound, upper_bound, bound_incl, sig_fig
):
    while angle <= upper_bound:
        angle += period
        append_solution(solutions, angle, lower_bound, upper_bound, bound_incl, sig_fig)


def append_left(
    solutions, angle, period, lower_bound, upper_bound, bound_incl, sig_fig
):
    while angle >= lower_bound:
        angle -= period
        append_solution(solutions, angle, lower_bound, upper_bound, bound_incl, sig_fig)


def arcsin_in_range(ratio, lower_bound, upper_bound, bound_incl=True, sig_fig=3):
    solutions = []
    x1 = degrees(asin(ratio))
    append_solution(solutions, x1, lower_bound, upper_bound, bound_incl, sig_fig)
    append_right(solutions, x1, 360, lower_bound, upper_bound, bound_incl, sig_fig)
    append_left(solutions, x1, 360, lower_bound, upper_bound, bound_incl, sig_fig)

    x2 = 180 - x1
    append_solution(solutions, x2, lower_bound, upper_bound, bound_incl, sig_fig)
    append_right(solutions, x2, 360, lower_bound, upper_bound, bound_incl, sig_fig)
    append_left(solutions, x2, 360, lower_bound, upper_bound, bound_incl, sig_fig)

    return sorted(solutions)


def arccos_in_range(ratio, lower_bound, upper_bound, bound_incl=True, sig_fig=3):
    solutions = []
    x1 = degrees(acos(ratio))
    append_solution(solutions, x1, lower_bound, upper_bound, bound_incl, sig_fig)
    append_right(solutions, x1, 360, lower_bound, upper_bound, bound_incl, sig_fig)
    append_left(solutions, x1, 360, lower_bound, upper_bound, bound_incl, sig_fig)

    x2 = -x1
    append_solution(solutions, x2, lower_bound, upper_bound, bound_incl, sig_fig)
    append_right(solutions, x2, 360, lower_bound, upper_bound, bound_incl, sig_fig)
    append_left(solutions, x2, 360, lower_bound, upper_bound, bound_incl, sig_fig)

    return sorted(solutions)


def arctan_in_range(ratio, lower_bound, upper_bound, bound_incl=True, sig_fig=3):
    solutions = []
    x1 = degrees(atan(ratio))
    append_solution(solutions, x1, lower_bound, upper_bound, bound_incl, sig_fig)
    append_right(solutions, x1, 180, lower_bound, upper_bound, bound_incl, sig_fig)
    append_left(solutions, x1, 180, lower_bound, upper_bound, bound_incl, sig_fig)

    return sorted(solutions)


def validate_selection(num):
    try:
        return int(num) if int(num) in [0, 1, 2, 3] else -1
    except Exception as e:
        print(e)
        return -1


def eval_expression(expression):
    code = compile(expression, "<string>", "eval")
    if code.co_names:
        raise NameError(f"Use of names not allowed")
    return eval(code, {"__builtins__": {}}, {})


def validate_numbers(num):
    try:
        return float(num)
    except Exception:
        try:
            return eval_expression(num)
        except Exception as e:
            raise Exception(e)


def yn_bool(txt):
    txt = txt.strip()
    if len(txt) == 0:
        # default
        return True
    elif txt[0].upper() in ["N", "F"]:
        return False
    else:
        return True


def main():
    selection = -1  # initialise
    while selection != 0:
        print("Select which inverse trigonometric function you require:")
        print("\t1. asin")
        print("\t2. acos")
        print("\t3. atan")
        print("\t0. exit")

        selection = validate_selection(input("\nChoose 1/2/3/0: "))
        if selection == 0:
            print("Good bye!")
            break
        if selection > 0:
            funcs = ["exit", "asin", "acos", "atan"]
            print("You have selected: {}".format(funcs[selection]))
            ratio = validate_numbers(input("\tEnter the trigonometric ratio: "))
            print("Provide the boundaries for the solution interval")
            lbound = validate_numbers(input("\tEnter lower boundary (in degrees): "))
            ubound = validate_numbers(input("\tEnter upper boundary (in degrees): "))
            incl_bounds = yn_bool(input("\tInclude boundaries? (default=Yes) Y/n: "))

        if selection == 1:
            soln = arcsin_in_range(
                ratio, min(lbound, ubound), max(lbound, ubound), bound_incl=incl_bounds
            )
        elif selection == 2:
            soln = arccos_in_range(
                ratio, min(lbound, ubound), max(lbound, ubound), bound_incl=incl_bounds
            )
        elif selection == 3:
            soln = arctan_in_range(
                ratio, min(lbound, ubound), max(lbound, ubound), bound_incl=incl_bounds
            )
        else:
            print("Instruction unknown.")
        print("\nSolutions: {}".format(soln))
        print()


def plot_solutions(function, solutions, lbound, ubound):
    pass


if __name__ == "__main__":
    main()
