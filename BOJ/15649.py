import sys 
from itertools import permutations
if __name__ == '__main__':
    input = sys.stdin.readline
    n, m = map(int, input().split())
    for permu in permutations(range(1,n+1), m):
        print(*permu)