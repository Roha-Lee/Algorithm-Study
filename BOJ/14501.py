# 내일 맑은 정신일때 코드 깔끔하게 만들기 
import sys 
def get_max_profit(table):
    n = len(table)
    DP = [0] * n
    DP[-1] = table[-1][1] if table[-1][0] == 1 else 0
    
    for i in range(n-2, -1, -1):
        duration, profit = table[i]
        prev_val = 0 if i + duration >= n else DP[i + duration]
        profit = 0 if i + duration > n else profit
        DP[i] = max(profit + prev_val, DP[i+1])
    
    return DP[0]

if __name__ == '__main__':
    input = sys.stdin.readline
    n = int(input())
    table = []
    for _ in range(n):
        duration, profit = map(int, input().split())
        table.append((duration, profit))
    print(get_max_profit(table))