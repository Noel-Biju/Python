def fibonacci(n):
    sequnce=[]
    first_number,second_number=0,1
    for _ in range(n):
        sequnce.append(first_number)
        first_number,second_number=second_number,first_number+second_number
    return sequnce

