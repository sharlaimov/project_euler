#http://projecteuler.net/problem=4
#A palindromic number reads the same both ways. 
#The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 ? 99.
#Find the largest palindrome made from the product of two 3-digit numbers.

num1 = list(range(999,99,-1))
num2 = list(range(999,99,-1))

palindroms=[]
it_num = 0
def is_palindrom(n):
    return  str(n)==str(n)[::-1]

for n1 in num1:
    for n2 in num2:
        it_num+=1
        if n1 < num2[len(num2)-1]:
            break
        if is_palindrom(n1*n2):
            palindroms.append(n1*n2)
            print(str(n1) +'*'+str(n2)+'='+str(n1*n2))
            del num2[num2.index(n2):]

print('answer : '+str(max(palindroms)))
print('iterations : ' +str(it_num))