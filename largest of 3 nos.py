n1=int(input("Enter First Number:"))
n2=int(input("Enter Second Number:"))
n3=int(input("Enter Third Number:"))
if n1>n2 and n1>n3:
    print("The largest number is",n1)
elif n2>n3 and n2>n1:
    print("The largest number is",n2)
else:
    print("The largest number is",n3)
