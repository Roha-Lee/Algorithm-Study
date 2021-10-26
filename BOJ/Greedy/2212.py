import sys 
input = sys.stdin.readline
n = int(input())
k = int(input())
sensors = sorted(list(map(int, input().split())))

if n == 1:
    print(0)
else:
    gaps = sorted([sensors[i] - sensors[i-1] for i in range(1, n)])
    for _ in range(k-1):
        gaps.pop()
    print(sum(gaps))
