import random
data = list(range(10))
random.shuffle(data)
count = [0] * (max(data) + 1)
for item in data:
    count[item] += 1

for idx, cnt in enumerate(count):
    for _ in range(cnt):
        print(idx, end=' ')   
print()