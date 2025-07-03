#implementation of quick sort (divide and conquer technique)
#12 elem = unsorted, 8 elem = increasing,sorted but 1, 6 elem = decreasing,sorted
def quick_sort(array, low, high):
    if low < high:
        pivot_index = partition(array, low, high)
        quick_sort(array, low, pivot_index-1)
        quick_sort(array, pivot_index+1, high)
        return array

def partition(array, low, high):
    pivot_index = array[high]
    k = low
    for i in range(low, high):
        if array[i] < pivot_index:
            array[i], array[k] = array[k], array[i]
            k += 1
    array[k], array[high] = array[high], array[k]
    return k

arr1 = [5, 1, 6, 2, 7, 4, 43, 26, 88, 22, 64, 12]
arr2 = [7, 8, 9, 11, 10, 12]
arr3 = [6, 5, 4, 3, 2, 1]
result1 = quick_sort(arr1, 0, len(arr1)-1)
result2 = quick_sort(arr2, 0, len(arr2)-1)
result3 = quick_sort(arr3, 0, len(arr3)-1)
print(result1)
print(result2)
print(result3)