import sys 
input = sys.stdin.readline

n = int(input())
cranes = sorted(list(map(int, input().split())), reverse=True)
m = int(input())
boxes = sorted(list(map(int, input().split())), reverse=True)
cache = [0] * n
done = [False] * m

if boxes[0] > cranes[0]:
    print(-1)
else:
    time = 0
    while sum(done) < m:
        for i in range(n):
            for j in range(cache[i], m):
                cache[i] = j + 1 if j < m else m
                if cranes[i] >= boxes[j] and not done[j]:
                    done[j] = True
                    break
        time += 1
    print(time)

