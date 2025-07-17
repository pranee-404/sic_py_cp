#list partitioning to count number of values of p so that x>p and y<p
N = int(input('Enter the number of elements: '))
x = int(input('Enter the value of X: '))
y = int(input('Enter the value of Y: '))
if x + y == N:
    numbers = list(map(int,input('Enter the numbers: ').split()))
    if len(numbers) == N:
        numbers.sort()
        p = numbers[y] - numbers[y-1] - 1
        print(p)