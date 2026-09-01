def find_largest(arr):
    largest = arr[0]
    for i in arr:
        if i > largest:
            largest = i
    return largest
arr = [10,45,9, 67, 34, 89, 23]
result = find_largest(arr)
print("The largest element in the array is:", result)
