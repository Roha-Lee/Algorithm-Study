import random
data = [1,2,3,4,5,6,7,8,9,0]
random.shuffle(data)

def quick_sort(data, start = 0, end = len(data)-1):
    if start >= end:
        return 
    pivot = start
    left = start + 1
    right = end

    while left <= right:
        while left <= end and data[left] <= data[pivot]:
            left += 1
        while right > start and data[right] >= data[pivot]:
            right -= 1
        if left > right:
            data[right], data[pivot] = data[pivot], data[right]
        else:
            data[left], data[right] = data[right], data[left]
    
    quick_sort(data, start, right-1)
    quick_sort(data, right+1, end)
    
quick_sort(data)
print(data)