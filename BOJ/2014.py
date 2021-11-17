import sys 
from heapq import heappop, heappush, heapify
if __name__ == '__main__':
    input = sys.stdin.readline
    k, n = map(int, input().split())
    primes = list(map(int, input().split()))
    candidates = primes[:]
    heapify(candidates)
    for i in range(n):
        curr = heappop(candidates)
        for j in range(k):
            val = curr * primes[j]
            heappush(candidates, val)
            if curr % primes[j] == 0: # <- 이걸 어떻게 생각하지..
                break
    print(curr)
    