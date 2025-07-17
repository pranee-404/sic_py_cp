#Hollow Rhombus
n = int(input('Enter the number of lines: '))
for i in range(1,n+1):
    if i == 1:
        print(' '*(n-1) + '* '*n)
    elif i == n:
        print('* '*n)
    else:
        print(' '*(n-i) + '*' + ' '*(2*n-3) + '*')