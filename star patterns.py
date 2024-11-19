n=int(input("Enter the no of rows:"))
#Increasing Triangle
for i in range(n+1):
    for j in range(i):
        print("*",end=" ")
    print()
print("\n")
#Deacreasing Triangle
for i in range(n,0,-1):
    for j in range(i):
        print("*",end=" ")
    print()
#Hill Pattern
for i in range(n+1):
    for j in range(n-i):
        print(" ",end=" ")
    for k in range(2*i-1):
        print("*",end=" ")
    print()
print("\n")
#Reverse Hill Pattern
for i in range(n,0,-1):
    for j in range(n-i):
        print(" ",end=" ")
    for k in range(2*i-1):
        print("*",end=" ")
    print()
