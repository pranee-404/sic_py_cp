#binary search using recursion
def binary(li,low,high,key):
    li.sort()
    if low <= high:
        mid = (low + high) // 2
        if li[mid] == key:
            return mid
        elif li[mid] < key:
            return binary(li, mid+1,high,key)
        elif li[mid] > key:
            return binary(li,low,mid-1,key)
        
list2 = [5, 6, 9, 4, 3, 1]
print(binary(list2,0,len(list2)-1,9))