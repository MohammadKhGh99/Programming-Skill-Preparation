# 1 - Write a program to reverse a string in place.
# naive way
def reverse_string_in_place(text):
    print("The String Before Reversing: " + text)
    for i in range(len(text)):
        text = text[:i] + text[-1] + text[i:-1]
    print("The String  After Reversing: " + text)
    print()
    return text


# built-in operations
# def reverse_string_in_place_fast(text):
#     # text = reversed(text)
#     text = text[::-1]
#     return text


# 2 - Write a program to find the maximum and minimum elements in an array.
def find_min_max(arr):
    print("The Array: " + str(arr))
    minimum = arr[0]
    maximum = arr[0]
    for x in arr:
        if x < minimum:
            minimum = x
        if x > maximum:
            maximum = x

    print("Minimum Number in Array is: " + str(minimum))
    print("Maximum Number in Array is: " + str(maximum))
    print()

    return minimum, maximum


# 3 - Write a program to remove duplicates from a sorted array.
def remove_duplicates(arr):
    print("The Array: " + str(arr))
    i = 0
    length = len(arr)
    while i < length - 1:
        if arr[i] == arr[i + 1]:
            arr.remove(arr[i])
            length = len(arr)
            continue
        i += 1

    print("The Array After Removing Duplicates is: " + str(arr))
    return arr


if __name__ == '__main__':
    txt = "abcdefg"
    reverse_string_in_place(txt)

    arr = [20, 10, 20, 4, 100]
    find_min_max(arr)

    arr = [1, 1, 2, 3, 4, 4, 4, 4, 5, 6, 6, 7, 7, 8, 8, 9, 9, 9, 9, 9]
    remove_duplicates(arr)
