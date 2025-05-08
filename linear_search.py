def linear_search(arr, target):
    for index, value in enumerate(arr):
        if value == target:
            return index  # Target found
    return -1  # Target not found

# Example usage:
arr = [5, 3, 8, 6, 7, 2]
target = 6

result = linear_search(arr, target)
if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found")