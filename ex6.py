# 1 - Implement the linear search algorithm.
def linear_search(array: list, item: int):
    for i in range(len(array)):
        if array[i] == item:
            return i
    return -1


# 2 - Implement the binary search algorithm.
def binary_search_recursive(array: list, item: int):
    if len(array) == 0:
        return -1
    if len(array) == 1:
        return array[0] if array[0] == item else -1
    
    mid = len(array) // 2
    if array[mid] == item:
        return mid
    if item > array[mid]:
        return binary_search_recursive(array[mid:], item)
    elif item < array[mid]:
        return binary_search_recursive(array[:mid], item)
    return -1


def binary_search_iterative(array: list, item: int):
    left, right, mid = 0, len(array) - 1, len(array) // 2
    while left <= right:
        mid = (left + right) // 2
        if array[mid] == item:
            return mid
        elif item < array[mid]:
            right = mid - 1
        else:  # >
            left = mid + 1
    return -1
    

if __name__ == '__main__':
    # Question 1
    array = [38, 27, 43, 3, 9, 82, 10]
    print("The Array: " + str(array))
    print()
    print("Searching for (9) using Linear Search: " + str(linear_search(array, 9)))
    print()
    
    # Question 2
    # in binary search the array should be sorted
    binary_array = sorted(array)
    print("Sorted Array: " + str(binary_array))
    print()
    print("Searching for (9) using Recursive Binary Search: " + str(binary_search_recursive(binary_array, 9)))
    print()
    print("Searching for (9) using iterative Binary Search: " + str(binary_search_iterative(binary_array, 9)))
    