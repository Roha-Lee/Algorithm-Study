# 1로 만들기 Top - down
# N = 26
# DP = [0] * (N+1)
# def make_one(num):
#     if num == 1:
#         return 0
#     if DP[num] != 0:
#         return DP[num]
#     candidate = []
#     if num%5 == 0:
#         candidate.append(make_one(num//5))
#     if num%3 == 0:
#         candidate.append(make_one(num//3))
#     if num%2 == 0:
#         candidate.append(make_one(num//2))
#     candidate.append(make_one(num-1))
#     DP[num] = min(candidate) + 1
#     return DP[num]
 
# print(make_one(N))

# 1로 만들기 Bottom up 방식 
N = 16
DP = [0] * (N+1)
for i in range(2, N+1):
    DP[i] = DP[i-1] + 1
    if i%5 == 0:
        DP[i] = min(DP[i//5] + 1, DP[i])
    if i%3 == 0:
        DP[i] = min(DP[i//3] + 1, DP[i])
    if i%2 == 0:
        DP[i] = min(DP[i//2] + 1, DP[i])
print(DP[N])
    