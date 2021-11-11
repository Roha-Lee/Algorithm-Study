from itertools import combinations
import sys 

if __name__ == '__main__':
    input = sys.stdin.readline
    n, m = map(int, input().split())
    for comb in combinations(range(1, n+1), m):
        print(*comb)