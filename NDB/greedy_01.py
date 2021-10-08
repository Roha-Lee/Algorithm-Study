N, K = map(int, input().split()) 

cnt = 0
while N:
    remainder = int(N % K)
    if remainder == 0:
        N //= K
        cnt += 1
    else:
        N -= remainder
        cnt += remainder

print(cnt - 1)