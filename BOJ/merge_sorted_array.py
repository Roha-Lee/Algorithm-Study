a = [1,4,7,8]
b = [2,3,5,6,7,8,9,10]
result = []
idx_a, idx_b = 0, 0
while idx_a < len(a) and idx_b < len(b):
    if a[idx_a] <= b[idx_b]:
        result.append(a[idx_a])
        idx_a += 1
    else:
        result.append(b[idx_b])
        idx_b += 1
if idx_b == len(b):
    result.extend(a[idx_a:])
if idx_a == len(a):
    result.extend(b[idx_b:])
print(result)