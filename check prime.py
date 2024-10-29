num=int(input("Enter the number:"))
i=0
for i in range(2,(num//2)+1):
    if num%i==0:
        break
if i==(num//2):
    print("The number is prime")
else:
    print("The number is not prime")
