data = list(range(10))

def binary_search(data, query, start=0, end=len(data)-1):
    if start > end:
        return None
    mid = (end + start) // 2
    if data[mid] < query:
        start = mid + 1
        return binary_search(data, query, start, end)
    elif data[mid] > query:
        end = mid - 1
        return binary_search(data, query, start, end)
    else:
        return mid

print(binary_search(data, 2))
print(binary_search(data, 11))