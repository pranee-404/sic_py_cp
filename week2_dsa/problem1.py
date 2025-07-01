#rotation string problem
original_str = input('Enter the original string: ')
rotated_str = input('Enter the rotated string: ')
#concatenate the rotated_str two times
temp_str = rotated_str * 2
if temp_str.find(original_str) != -1:
    print(1)
else:
    print(-1)