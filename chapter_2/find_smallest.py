def findSmallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

print(findSmallest([5, 3, 6, 2, 10]))  # => 3
print(findSmallest([60, 23, 33, 17, 10]))

# This code defines a function to find the index of the smallest element in an array.