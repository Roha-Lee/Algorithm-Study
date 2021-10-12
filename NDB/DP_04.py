# DP = [10001] * ( M + 1 )
# DP[0] = 0
# for i in range(N):
#     for j in range(coins[i], M+1):
#         if DP[j-coins[i]] != 10001:
#             DP[j] = min(DP[j], DP[j-coins[i]]+1)

# if DP[M] == 10001:
#     print(-1)
# else:
#     print(DP[M])

N, M = 3, 7 
coins = [2, 3, 5]
# N, M = 2, 15
# coins = [2,3]
DP = [-1] * (M + 1)
for i in range(1, M+1):
    candidates = [ i-coin for coin in coins if i-coin >= 0]
    if 0 in candidates:
        DP[i] = 1  
    elif candidates:
        values = [DP[candidate] for candidate in candidates if DP[candidate]>0]
        if values:
            DP[i] = min(values) + 1
print(DP[M])
