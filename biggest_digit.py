#Find biggest digit in a number
input_num = input('Enter the Number: ')
num_list = []
for i in input_num:
    num_list.append(i)
print('The Biggest Digit in', input_num, 'is', max(num_list))