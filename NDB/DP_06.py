
N = int(input())
powers = list(map(int, input().split()))

DP = [1] * N
for i in range(1, N):
    for j in range(0, i):
        if powers[j] > powers[i]:
            DP[i] = max(DP[i], DP[j]+1)
ans1 = N-max(DP)
print(ans1)