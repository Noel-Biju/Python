num=int(input("Enter the number:"))
isPrime=True
for i in range(2,num//2+1):
    if num%i==0:
        isPrime=False
        break
if isPrime:
    print("The given number is a prime")
else:
    print("The given number is a not prime")
