import sys 
input = sys.stdin.readline
N, r, c = map(int, input().split())
def find_loc(N, r, c):
    if N == 0:
        return 0
    _r = r // (2**(N-1))
    _c = c // (2**(N-1))
    return 2**(N-1) * 2**(N-1) * (2 * _r + _c) + find_loc(N-1, r%(2**(N-1)), c%(2**(N-1)))
print(find_loc(N, r, c))