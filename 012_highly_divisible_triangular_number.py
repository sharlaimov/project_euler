__author__ = 'ESharlaimov'

#http://projecteuler.net/problem=12
#The sequence of triangle numbers is generated by adding the natural numbers.
## So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:
#1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
#Let us list the factors of the first seven triangle numbers:
#1: 1
#3: 1,3
#6: 1,2,3,6
#10: 1,2,5,10
#15: 1,3,5,15
#21: 1,3,7,21
#28: 1,2,4,7,14,28
#We can see that 28 is the first triangle number to have over five divisors.
#What is the value of the first triangle number to have over five hundred divisors?

#brute

n = 1

while True:
    triangle_num = n * (n + 1) // 2
    counter = 0
    for i in range(1, triangle_num):
        if triangle_num % i == 0:
            counter += 1

        if i >= triangle_num ** .5:
            break

    counter *= 2
    if triangle_num % triangle_num ** 0.5 == 0:
        counter += 1

    if counter >= 500:
        break

    n += 1
    print(n)

print(counter)

