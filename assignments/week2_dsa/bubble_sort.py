#bubble sort implementation
#worst case efficiency is O(n^2)
arr = list(map(int,input('Enter the elements of the array: ').split()))
n = len(arr)
for i in range(0,n):
    for j in range(0,n-i-1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
print('The sorted array is: ',arr)