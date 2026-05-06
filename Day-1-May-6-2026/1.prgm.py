def sum_three_num(n1:int,n2:int,n3:int)->int:
    sum = n1+n2+n3
    return sum

n1 = int(input('Enter 1st number: '))
n2 = int(input('Enter 2cd number: '))
n3 = int(input('Enter 3rd number: '))

print(f"The given numbers are {n1}, {n2}, {n3} the sum is {sum_three_num(n1,n2,n3)}")