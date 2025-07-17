#implementation of optimised bubble sort
#best case efficiency is O(n)
arr = list(map(int,input('Enter the elements of the array: ').split()))
n = len(arr)
for i in range(0,n):
    sorted = True
    for j in range(0,n-i-1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
            sorted = False
    if sorted:
        break
print('The sorted array is: ',arr)