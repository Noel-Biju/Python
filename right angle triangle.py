def right_angle_triangle():
    side1=int(input("Enter the length of first side:"))
    side2=int(input("Enter the length of second side:"))
    side3=int(input("Enter the length of third side:"))
    sides=[side1,side2,side3]
    sides.sort()
    if sides[2]**2==sides[1]**2+sides[0]**2:
         print("It is a right triangle")
    else:
        print("It is not a right triangle")
right_angle_triangle()