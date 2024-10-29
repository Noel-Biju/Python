limit=int(input("Enter the limit:"))
for num in range(2,limit+1):
    isPrime=True
    for i in range(2,(num//2)+1):
        if num%i==0:
            isPrime=False
    if isPrime:
        print(num,end=" ")
