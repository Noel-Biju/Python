def check_mobile_number():
    num=input("Enter a mobile number:")
    if len(num)==10 and num[0]=='7':
        print("Valid number")
    elif len(num)==10 and num[0]=='8':
        print("Valid number")
    elif len(num)==10 and num[0]=='9':
        print("Valid number")
    else:
        print("Invalid number")
check_mobile_number()