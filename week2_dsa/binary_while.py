#binary search using a while loop
list1 = list(map(int, input('Enter the elements of the list: ').split()))
element = int(input('Enter the element to find: '))
list1.sort()
print('Sorted list:',list1)
low = 0
high = len(list1)-1
while low <= high:
    mid = (low + high) // 2
    if list1[mid] == element:
        print('Element found at position:',mid)
        break
    elif list1[mid] < element:
        low = mid + 1
    elif list1[mid] > element:
        high = mid - 1