from binary import binarySearch, arr

def exponentialSearch(key):
    if key == arr[0]:
        return f"{key} found at position 0 in arr."

    i = 1
    while i < len(arr) and arr[i] <= key:
        i *= 2

    return binarySearch(key, i // 2, min(len(arr), i))

exponentialSearch(6)
exponentialSearch(12)