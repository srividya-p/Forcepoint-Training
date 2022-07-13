arr = [2, 1, 4, 2, 6, 5, 7, 8, 9]

def linearSearch(key):
    for i in range(len(arr)):
        if arr[i] == key:
            return f"{key} found at position {i} in arr."
    
    return f"{key} not found in arr."

print(linearSearch(6))
print(linearSearch(12))