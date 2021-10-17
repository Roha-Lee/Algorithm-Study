import sys 
input = sys.stdin.readline
DP = [0] * 46
DP[1] = 1

def fibo(n):
    if n==0:
        return 0

    if DP[n] == 0:
        DP[n] = fibo(n-1) + fibo(n-2)
    return DP[n]
    
n = int(input())
print(fibo(n))

def fibo2(n):
    a, b = 0, 1
    for _ in range(n-1):
        a, b = b, a+b
    return b
print(fibo2(n))