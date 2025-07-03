#implementation of selection sort
array = list(map(int,input('Enter the elements of the array: ').split()))
n = len(array)
for i in range(1,n):
    element = array[i-1]
    position = i-1
    for j in range(i-1,n):
        if array[j] < element:
            element = array[j]
            position = j
    array[position], array[i-1] = array[i-1], array[position]
print('The sorted array is:',array)