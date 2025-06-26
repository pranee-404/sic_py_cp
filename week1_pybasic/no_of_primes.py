#Count number of Prime digits in a number
input_num = input('Enter the number: ')
count = 0
for i in input_num:
    k = int(i)
    if k > 2:
        for j in range(2,k):
            if k%j == 0:
                break
        else:
            count += 1
    elif k == 2:
        count += 1
print('The number of Prime digits in the number is', count)