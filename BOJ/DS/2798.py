# from itertools import permutations
# import sys 

# input = sys.stdin.readline
# n, m = map(int, input().split())
# cards = list(map(int, input().split()))
# candidates = permutations(cards, 3) 
# best = 0
# for candidate in candidates:
#     values = sum(candidate)  
#     if m - values >= 0 and values > best:
#         best = values
# print(best)

import sys 
input = sys.stdin.readline
n, m = map(int, input().split())
cards = list(map(int, input().split()))
best = 0
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            sum_val = cards[i] + cards[j] + cards[k]
            if m - sum_val >= 0 and sum_val > best:
                best = sum_val
print(best)


