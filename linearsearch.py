def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # return the index if found
    return -1  # return -1 if not found

# Example usage
arr = [10, 20, 30, 40, 50]
target = 30

result = linear_search(arr, target)

if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found")
