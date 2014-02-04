__author__ = 'ESharlaimov'

#http://projecteuler.net/problem=9

#A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

#a^2 + b^2 = c^2
#For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

#There exists exactly one Pythagorean triplet for which a + b + c = 1000.
#Find the product abc.

import math

squares = []

for i in range(1, 501):
    squares.append(i**2)


print(squares)

for b2 in squares:
    for a2 in squares[:squares.index(b2)]:
        if a2+b2 in squares:
            if squares.index(a2) + squares.index(b2) + squares.index(a2+b2) == 1000:
                print(squares.index(a2), squares.index(b2), squares.index(a2+b2))

