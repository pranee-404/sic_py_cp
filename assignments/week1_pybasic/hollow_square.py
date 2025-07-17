#Hollow Square
n = int(input('Enter the number of lines: '))
for i in range(1,n+1):
    if i == 1 or i == n:
        print('* '*n)
    else:
        print('*'+' '*(2*n-3)+'*')