#N = int(input('Enter the size of the array:'))
try:
    numbers = [float(num) for num in input('Enter the elements:').split()]
    print(numbers)
except ValueError as err:
    print('Invalid float number entered.')