list_1=[]
n1=int(input("How many elements in a list?:"))
print("The elements in list 1:")
for i in range(n1):
    list_1.append(int(input()))
    list_1.sort()
list_2=[]
n2=int(input("How many elements in a list?:"))
print("The elements in list 2:")
for i in range(n2):
    list_2.append(int(input()))
    list_2.sort()
list_3=list_1 + list_2
print(list_3)
even_list=[]
odd_list=[]
for i in list_3:
    if i%2==0:
        even_list.append(i)
    else:
        odd_list.append(i)
print(even_list)
print(odd_list)
combined_list=even_list+odd_list
print(combined_list)
