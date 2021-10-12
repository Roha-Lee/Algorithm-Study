# N = int(input())
# foods = list(map(int, input().split()))

def ant_food(foods):
    DP = [0] * len(foods)
    DP[0] = foods[0]
    DP[1] = max(foods[1], foods[0])
    for i in range(2, len(foods)):
        DP[i] = max(DP[i-1], DP[i-2] + foods[i])
    return DP[-1]
import random
foods = []
for i in range(100):
    foods.append(random.randint(0, 1000))
foods = [3,1]
print(ant_food(foods))