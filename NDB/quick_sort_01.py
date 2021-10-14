def quick_sort(data, start=0, end=None):
    if end is None: 
        end = len(data)-1
    if start >= end:
        return 
    p = start
    left = start + 1
    right = end
    while left<=right:
        while left <= end and data[p] >= data[left]:
            left += 1
        while right >=0 and data[p] < data[right]:
            right -= 1
        if left <= right: 
            data[left], data[right] = data[right], data[left]
        else:
            data[right], data[p] = data[p], data[right]
            p = right
    
    quick_sort(data, start, p-1)
    quick_sort(data, p+1, end)

import random
for j in range(100):
    leng = random.randint(1, 100)
    data = [0] * leng
    for i in range(leng):
        data[i] = random.randint(1, 100)
    original = data[:]
    original.sort()
    quick_sort(data)
    if not data == original:
        print(data)
        print(original)
        print("FAIL")
    else:
        print(f"test-{j} success")