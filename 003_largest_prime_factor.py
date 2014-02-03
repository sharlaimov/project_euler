#http://projecteuler.net/problem=3
#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?

num = 600851475143
prime_factors=[]

def is_prime(n):
  for prime in prime_factors:
    if n%prime == 0:
      return False
  return True

for i in range(2,int(num**(.5))):
  if num%i ==0 and is_prime(i):
    print(i)
    prime_factors.append(i)

print('Answer: '+str(prime_factors[len(prime_factors)-1]))