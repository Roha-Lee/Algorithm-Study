import random
data = [1,2,3,4,5,6,7,8,9,0]
random.shuffle(data)

for i in range(1, len(data)):
    for j in range(i, 0, -1):
        if data[j] < data[j-1]:
            data[j-1], data[j] = data[j], data[j-1]
        else:
            break
print(data)