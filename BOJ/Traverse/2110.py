import sys 
input = sys.stdin.readline
N, C = map(int, input().split())
locations = [int(input()) for _ in range(N)]
locations.sort()

start = 1
end = locations[-1] - locations[0]
best = 0
while start <= end:
    mid = (start + end) // 2
    next_elem = 0
    cnt = 0
    for loc in locations:
        if loc >= next_elem:
            next_elem = loc + mid
            cnt += 1
    
    if cnt >= C:
        start = mid + 1
        best = mid
    else:
        end = mid - 1

print(best)

