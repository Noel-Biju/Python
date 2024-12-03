#Factorial of a number
def factorial(n):
    if n==1:
        return 1
    else:
        return n*factorial(n-1)
print(factorial(5))
# Adding two positive numbers
def add_numbers(n1,n2):
    if n2==0:
        return n1
    else:
        return add_numbers(n1+1,n2-1)
print(add_numbers(5,4))
#Multiplying two numbers
def multiply(n1,n2):
    if n2==1:
        return n1
    else:
        return n1+multiply(n1,n2-1)
print(multiply(5,4))
#GCD
def gcd(n1,n2):
    if n1%n2==0:
        return n2
    else:
        return gcd(n2,n1%n2)
print(gcd(516,188))