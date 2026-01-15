def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return f"{target} found at position {mid}"
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return f"{target} not found"

numbers = [2, 5, 8, 12, 16, 23, 38]
print(binary_search(numbers, 16))
