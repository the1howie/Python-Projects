import math
import matplotlib.pyplot as plt
from decimal import Decimal, getcontext
from sympy import N

E_PRECISION = 10000

getcontext = E_PRECISION

compounding_period = {
    "annual": 1,
    "semi-annual": 2,
    "quarterly": 4,
    "monthly": 12,
    "daily": 365,
    "hourly": 365 * 24,
    "by-the-minute": 365 * 24 * 60,
    "by-the-second": 365 * 24 * 60 * 60,
    "by-the-millisecond": 365 * 24 * 60 * 60 * 1000,
    "by-the-microsecond": 365 * 24 * 60 * 60 * 1000 * 1000,
    "by-the-nanosecond": 365 * 24 * 60 * 60 * 1000 * 1000 * 1000,
    "by-the-picosecond": 365 * 24 * 60 * 60 * 1000 * 1000 * 1000 * 1000,
}


# compunding rate as a decimal number
rate = 1.0
print("compounding rate: {}%".format(rate * 100))

# target is e^x
target = Decimal(math.exp(rate))
print("target: {}\n".format(N(target, 40)))

# compounding interest multiplier
compounding = {}
for k, v in compounding_period.items():
    compounding[k] = Decimal((1 + Decimal(rate / v)) ** v)

x = list(range(len(compounding)))
xticks = []
y = []
e = []
est_errors = []

for k, v in compounding.items():
    err = Decimal(target - v)
    print("{}\t-\t{}\t-\terr {}".format(k, N(v, 20), N(err, 20)))
    xticks.append(k)
    y.append(v)
    e.append(target)
    est_errors.append(err)
print()

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(6, 3))

ax1.plot(x, e, "r:")
ax1.plot(x, y, "b-")
ax1.set_xticks(x, xticks, rotation=90)
ax1.set_title("Euler's const. estimates")

ax2.plot(x, est_errors, "r-")
ax2.set_xticks(x, xticks, rotation=90)
ax2.set_title("Estimation errors")
plt.show()
