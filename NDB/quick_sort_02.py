import random
data = list(range(10))
random.shuffle(data)

def quick_sort(data):
    if len(data) <= 1:
        return data
    pivot = data[0]
    tail = data[1:]

    left = [x for x in tail if x <= pivot]
    right = [x for x in tail if x > pivot]

    return quick_sort(left) + [pivot] + quick_sort(right)

print(quick_sort(data))
