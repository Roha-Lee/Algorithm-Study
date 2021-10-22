import sys 
input = sys.stdin.readline
n = int(input())
DP = [1, 2]
for i in range(1,n):
    prev = DP[1]
    DP[1] = (DP[0] + DP[1]) % 15746
    DP[0] = prev
    
print(DP[0])