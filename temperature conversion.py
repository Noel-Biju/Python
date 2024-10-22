temp=int(input("Enter Temperature:"))
a=input("Is this in (C)elsius or (F)ahrenheit?")
if a=='C'or a=='c':
    f=(9/5)*temp+32
    print(temp,"Celsius is", f,"Fahrenheit")
elif a=='F' or a=='f':
    c=(5/9)*(temp-32)
    print(temp,"Fahrenheit is",c,"Celsius")
else:
    print("Invalid Temperature")

