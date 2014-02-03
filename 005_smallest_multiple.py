#http://projecteuler.net/problem=5
#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

prime_numbers = []
dividers = range(2, 21)
composite_factors = []

for n in dividers:

    prime_dividers = []
    original = n

    for prime in prime_numbers:
        while n % prime == 0:
            n /= prime
            prime_dividers.append(prime)

    if n == original:
        prime_numbers.append(original)
        prime_dividers.append(n)

    composite_factors.append(prime_dividers)

factors = []
while composite_factors:
    current_composite = composite_factors.pop()
    while current_composite:
        factor = current_composite.pop()
        for composite in composite_factors:
            if factor in composite:
                composite.remove(factor)
        factors.append(factor)

answer = 1

for f in factors:
    answer *= f

print(answer)
