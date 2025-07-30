"""
Estimation of Euler's number e from compounding interest.

            n
    ⎛    1⎞
lim  1 + ─    =  e
n→∞ ⎝    n⎠

Made possible with the use of https://mpmath.org/
"""

import os
import mpmath as mp


# calculation precision
E_DPS = 100000
mp.mp.dps = E_DPS

# for printing
SIGNIFICANT_DIGITS = 30


compounding_period = {
    "annual": mp.mpf(1),
    "semi-annual": mp.mpf(2),
    "quarterly": mp.mpf(4),
    "monthly": mp.mpf(12),
    "daily": mp.mpf(365),
    "hourly": mp.mpf(365) * mp.mpf(24),
    "by-the-minute": mp.mpf(365) * mp.mpf(24) * mp.mpf(60),
    "by-the-second": mp.mpf(365) * mp.mpf(24) * mp.power(60, 2),
    "by-the-millisecond": mp.mpf(365) * mp.mpf(24) * mp.power(60, 2) * mp.power(10, 3),
    "by-the-microsecond": mp.mpf(365) * mp.mpf(24) * mp.power(60, 2) * mp.power(10, 6),
    "by-the-nanosecond": mp.mpf(365) * mp.mpf(24) * mp.power(60, 2) * mp.power(10, 9),
    "by-the-picosecond": mp.mpf(365) * mp.mpf(24) * mp.power(60, 2) * mp.power(10, 12),
    "by-the-femtosecond": mp.mpf(365) * mp.mpf(24) * mp.power(60, 2) * mp.power(10, 15),
    "by-the-attosecond": mp.mpf(365) * mp.mpf(24) * mp.power(60, 2) * mp.power(10, 18),
    "by-the-zeptosecond": mp.mpf(365) * mp.mpf(24) * mp.power(60, 2) * mp.power(10, 21),
    "by-the-yoctosecond": mp.mpf(365) * mp.mpf(24) * mp.power(60, 2) * mp.power(10, 24),
}


def set_precision(N=E_DPS):
    mp.mp.dps = N


def compound_interest(period, principal=1, rate=1.0):
    # P * (1 + r/n)^n
    return mp.fmul(principal, mp.power(mp.fadd(1, mp.fdiv(rate, period)), period))


def do_calculation(key, value):
    temp = {}
    calc = compound_interest(value)
    temp["label"] = key
    temp["period"] = value
    temp["value"] = calc
    temp["error"] = mp.fsub(mp.e, calc)
    return temp


def do_all_calculations():
    set_precision()
    calculations = []
    for k, v in compounding_period.items():
        calculations.append(do_calculation(k, v))
    return calculations


def get_result_string(label, value, error, n):
    return f"{label:>22}\tcalc: {mp.nstr(value, n):<{n+7}} err: {mp.nstr(error, n)}"


def main():
    os.system("cls" if os.name == "nt" else "clear")

    n = SIGNIFICANT_DIGITS
    print(f"TARGET: {mp.nstr(mp.e, n)}\n")

    set_precision()
    calculations = []
    for k, v in compounding_period.items():
        item = do_calculation(k, v)
        calculations.append(item)
        print(get_result_string(item["label"], item["value"], item["error"], n))
    print()


if __name__ == "__main__":
    main()
