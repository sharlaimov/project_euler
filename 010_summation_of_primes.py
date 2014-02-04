__author__ = 'ESharlaimov'

# http://projecteuler.net/problem=10
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

primes = []


def is_prime(n):
    if n == 1:
        return False

    for prime in primes:
        if n % prime == 0:
            return False

        if prime * prime > n:
            return True

    return True


i = 2
res = 0
while i < 2000000:
    print(i)
    if is_prime(i):
        primes.append(i)
        res += i
    i += 1

print(res)

