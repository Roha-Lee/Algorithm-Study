import sys 
from heapq import heappush, heappop

if __name__ == '__main__':
    input = sys.stdin.readline
    q = []
    n = int(input())
    for _ in range(n):
        usr_input = int(input())
        if usr_input == 0:
            if q:
                val, sign = heappop(q)
                print(sign * val)
            else:
                print(0)
        else:
            heappush(q, (abs(usr_input), 1 if usr_input >= 0 else -1))
    