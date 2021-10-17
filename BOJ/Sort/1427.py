import sys 
input = sys.stdin.readline
N = list(input().rstrip())
N = sorted(N, reverse = True)
print(''.join(N))