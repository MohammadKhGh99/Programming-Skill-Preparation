# 1 - Implement the bubble sort algorithm.
def bubble_sort(array: list):
    # move on each element in array
    for i in range(len(array)):
        # move on each element in array except elements in indexes 0 - i and compare with i'th element
        for j in range(i + 1, len(array)):
            if array[i] > array[j]:
                array[i], array[j] = array[j], array[i]
    return array


# 2 - Implement the merge sort algorithm.
def merge_sort(array: list):
    if len(array) <= 1:
        return array
    
    # take the half of the array (left half and right half)
    mid = len(array) // 2
    left_subarray = array[:mid]
    right_subarray = array[mid:]
    
    # merge sort the left half of the array
    left_subarray = merge_sort(left_subarray)
    # merge sort the right half of the array
    right_subarray = merge_sort(right_subarray)
    
    # move on both left and right halves and merge their elements in one large sorted array
    l, r = 0, 0
    i = 0
    while l < len(left_subarray) and r < len(right_subarray):
        if left_subarray[l] < right_subarray[r]:
            array[i] = left_subarray[l]
            l += 1
        elif left_subarray[l] > right_subarray[r]:
            array[i] = right_subarray[r]
            r += 1
        i += 1
        
    # if remains elements in the left half
    while l < len(left_subarray):
        array[i] = left_subarray[l]
        l += 1
        i += 1
    
    # if remains elements in the right half
    while r < len(right_subarray):
        array[i] = right_subarray[r]
        r += 1
        i += 1
        
    return array
    

# 3 - Implement the quicksort algorithm.
def partition(array: list, low: int, high: int):
    # take the last element as the pivot of the array
    pivot = array[high]
    i = low - 1
    for j in range(low, high):
        # if the current element is smaller than pivot so switch i'th element and j'th element
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]
            
    array[i + 1], array[high] = array[high], array[i + 1]
    return i + 1


def quick_sort(array: list, low: int, high: int):
    if low < high:
        # take the new index of the pivot of the array
        pivot = partition(array, low, high)
        # sort the left half of the array in the same way
        array = quick_sort(array, low, pivot - 1)
        # sort the right half of the array in the same way
        array = quick_sort(array, pivot + 1, high)
    return array


if __name__ == '__main__':
    # Question 1
    bubble_array = [38, 27, 43, 3, 9, 82, 10]
    print("Before Bubble Sorting: " + str(bubble_array))
    bubble_array = bubble_sort(bubble_array)
    print("After  Bubble Sorting: " + str(bubble_array))
    print()
    
    # Question 2
    merge_array = [38, 27, 43, 3, 9, 82, 10]
    print("Before Merge Sorting: " + str(merge_array))
    merge_array = merge_sort(merge_array)
    print("After  Merge Sorting: " + str(merge_array))
    print()
    
    # Question 3
    quick_array = [38, 27, 43, 3, 9, 82, 10]
    print("Before Quick Sorting: " + str(quick_array))
    quick_array = quick_sort(quick_array, 0, len(quick_array) - 1)
    print("After  Quick Sorting: " + str(quick_array))
