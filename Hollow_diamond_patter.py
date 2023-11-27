for row in range(0,7):
    for column in range(0,7):
        if row+column==3 or column-row==3 or row-column==3 or column+row==9:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

print(" ")

for row in range(0,4):
    for column in range(0,4):
        if row==0 or row==3 or column==0 or column==3 :
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
print(" ")
for row in range(0,7):
    for column in range(0,7):
        
        print("*",end=" ")
        
    print()
print(" ")

import math
n=5
def factorial(n):
    return(math.factorial(n))
print(factorial(n))

print(" ")

n=6
def fact(n):
    if n==0 or n==1:
        return 1
    else:
        return n*fact(n-1)
print(fact(n))

print(" ")

n=5
def fibo(n):
    if n==1 or n<1:
        return n
    else:
        return fibo(n-1)+fibo(n-2)
for i in range (n):
    print(fibo(i))
print(" ")

# reverse the number
n=123456
reverse=0
while n!=0:
    num=n%10
    reverse=reverse*10+num
    n//=10            
print(reverse)

print(" ")

# Quadratic equation
import cmath
def root(a,b,c):
    d=(b**2)-(4*a*c)
    if d<0:
        print("given equation roots are imaginary")
        print((-b)/(2*a),"+i",cmath.sqrt(d))
    elif d==0:
        print("roots are equal")
        print((-b)/(2*a))
    else:
        print("roots are distinct but real")
        print(((-b)+cmath.sqrt(d))/(2*a))
        print(((-b)-cmath.sqrt(d))/(2*a))
print(root(3,4,4))

print(" ")

# Armstrong number
n=153
m=n
s=0
while n>0:
    r=n%10
    s=s+r**3
    n//=10
if s==m:
    print("armstrong")
else:
    print("no is not armstrong")
