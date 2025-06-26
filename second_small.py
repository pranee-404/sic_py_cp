#Find 2nd smallest digit in a number
input_num = input('Enter the Number: ')
num_digits = []
for i in input_num:
    num_digits.append(i)
smallest = min(num_digits)
while smallest in num_digits:
    num_digits.remove(smallest)
print('The Second smallest digit in the Number is: ', min(num_digits))