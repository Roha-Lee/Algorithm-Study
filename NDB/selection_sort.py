import random
data = [1,2,3,4,5,6,7,8,9,0]
random.shuffle(data)

for i in range(len(data)-1):
    min_index = i
    for j in range(i+1, len(data)):
        if data[min_index] > data[j]:
            min_index = j
    data[i], data[min_index] = data[min_index], data[i]
print(data)