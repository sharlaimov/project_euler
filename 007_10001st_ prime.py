#http://projecteuler.net/problem=7
#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

#What is the 10 001st prime number?


#bruteforce power

primes = []
num = 2


def is_prime(n):
    for prime in primes:
        if n % prime == 0:
            return False
    return True


while len(primes) != 10001:
    if is_prime(num):
        primes.append(num)
    num += 1

print(primes[10000])


