def fibonacci_search(arr, x):
    n = len(arr)
    # Initialize fibonacci numbers
    fibMMm2 = 0  # (m-2)'th Fibonacci No.
    fibMMm1 = 1  # (m-1)'th Fibonacci No.
    fibM = fibMMm2 + fibMMm1  # m'th Fibonacci

    # fibM is going to store the smallest Fibonacci
    # number greater than or equal to n
    while fibM < n:
        fibMMm2 = fibMMm1
        fibMMm1 = fibM
        fibM = fibMMm2 + fibMMm1

    # Marks the eliminated range from front
    offset = -1

    # while there are elements to be inspected
    while fibM > 1:
        i = min(offset + fibMMm2, n - 1)

        if arr[i] < x:
            fibM = fibMMm1
            fibMMm1 = fibMMm2
            fibMMm2 = fibM - fibMMm1
            offset = i
        elif arr[i] > x:
            fibM = fibMMm2
            fibMMm1 = fibMMm1 - fibMMm2
            fibMMm2 = fibM - fibMMm1
        else:
            return i

    # comparing the last element with x
    if fibMMm1 and offset + 1 < n and arr[offset + 1] == x:
        return offset + 1

    return -1

# Example usage:
arr = [10, 22, 35, 40, 45, 50, 80, 82, 85, 90, 100]
x = 85
result = fibonacci_search(arr, x)
print("Found at index:" if result != -1 else "Not found", result)