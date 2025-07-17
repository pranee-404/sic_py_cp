#Find the Nth Fibo (HemaChandra) term. Assume 1st 2 terms are 1 and 2
N = int(input('Enter the number N: '))
if N == 0 or N == 1 or N == 2:
    print('The Nth Fibonacci term is',N)
else:
    first, second = 1,2
    for i in range(3,N+1):
        sum = first + second
        first,second = second,sum
    print('The Nth Fibonacci term is',sum)    