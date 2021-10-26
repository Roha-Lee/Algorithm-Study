import sys
def dfs(cr, cc, count = 1):
    global curr_max
    if curr_max < count:
        curr_max = count

    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for dr, dc in moves:
        nr, nc = cr + dr, cc + dc
        if 0 <= nr < r and 0 <= nc < c and wordmap[nr][nc] not in used:
            used.add(wordmap[nr][nc])
            dfs(nr, nc, count + 1)
            used.remove(wordmap[nr][nc])
            
input = sys.stdin.readline
r, c = map(int, input().split())
wordmap = [[] for _ in range(r)]
for i in range(r):
    wordmap[i] = list(input().rstrip())
used = set([wordmap[0][0]])
curr_max = 0
dfs(0, 0)

print(curr_max)
