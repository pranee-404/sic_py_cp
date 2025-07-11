#Find biggest digit in a number
import pdb
pdb.set_trace()

input_num = input('Enter the list of numbers: ')
num_list = []
for i in input_num:
    num_list.append(i)
print('The Biggest Digit in', input_num, 'is', max(num_list))