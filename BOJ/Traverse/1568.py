import sys 
input = sys.stdin.readline
n = int(input())
cnt = 0
while n > 0:
    for i in range(int((2*n) ** 0.5) + 1 , -1, -1):
        val = i * (i+1) // 2
        if val <= n:     
            cnt += i
            n -= val
            break
    
print(cnt)