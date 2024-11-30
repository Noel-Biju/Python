def upper_and_lower(str):
    upper=0
    lower=0
    num=0
    for i in str:
        if i.isupper():
            upper+=1
        elif i.islower():
            lower+=1
        elif i.isdigit():
            num+=1
    print("No of uppercases is",upper)
    print("No of lower cases is",lower)
    print("No of digits is",num)
upper_and_lower(str=input("Enter a string:"))
