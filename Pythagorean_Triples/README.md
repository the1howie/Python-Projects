Formula for generating Primitive Pythagorean Triples
---------------------------------------------------------------------------------
INPUTS: The number of gradients 'm' is the input to this program.

The 'formula' is achieved by solving a system of two equations:
x^2 + y^2 = 1
y = mx + m, where m must be rational.

Solutions to this non-linear systems are:
(-1, 0) - This is the point that the line must pass throught.
((1-m^2)/(1+m^2), 2m/(1+m^2)(1+m^2)) - The x and y coordinate provide us with a
'formula' for generting Pythagorean triples.

Conditions: m = k/n where k, n are positive integers with k < n AND gcd(k,n) = 1.

The program generates nCr(n, 2) combinations of Pythagorean triples based on n.
These combinations are then filters by the conditions above.

Inspired by Polar Pi's great video: https://www.youtube.com/watch?v=y718ckf336c

As a bonus, I have included my spreadsheet that I programmed in VBA with my own 
algorithm based on https://en.wikipedia.org/wiki/Pythagorean_triple#:~:text=a%20is%20even.-,Elementary%20properties%20of%20primitive%20Pythagorean%20triples,-%5Bedit%5D

Enjoy.
