arr = [1, 3, 5, 6, 8, 9, 10, 11, 15]

def binarySearch(key, l = 0, r = len(arr) - 1):
    while l < r:
        mid = l + (r - l) // 2
        if arr[mid] == key:
            return f"{key} found at position {mid} in arr."
        elif key < arr[mid]:
            r = mid
        else:
            l = mid + 1

    return f"{key} not found in arr."

print(binarySearch(6))
print(binarySearch(12))