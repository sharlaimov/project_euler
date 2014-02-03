#http://projecteuler.net/problem=6

#The sum of the squares of the first ten natural numbers is,
#1^2 + 2^2 + ... + 10^2 = 385

#The square of the sum of the first ten natural numbers is,
#(1 + 2 + ... + 10)^2 = 55^2 = 3025

#Hence the difference between the sum of the squares of the first ten natural numbers 
#and the square of the sum is 3025 - 385 = 2640.

#Find the difference between the sum of the squares of the first one hundred natural numbers
#and the square of the sum.

mul1 = range(1, 101)
mul2 = range(1, 101)
res = 0

#Квадрат суммы n слагаемых равен сумме их квадратов плюс удвоенная сумма всевозможных попарных произведений
# этих слагаемых вида a_ia_j, где i<j.

for i in mul1:
    for j in mul2:
        if i != j and i < j:
            res += 2*i*j

print(res)