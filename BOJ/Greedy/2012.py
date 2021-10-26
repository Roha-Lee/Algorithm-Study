import sys 
input = sys.stdin.readline
n = int(input())
err = 0
scores = sorted([int(input()) for _ in range(n)])

for i in range(1, n+1):
    err += abs(i-scores[i-1])
    
print(err)