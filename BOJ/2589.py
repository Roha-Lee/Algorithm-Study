import sys 
from collections import deque
def find_longest_path(treasure_map, src):
    height = len(treasure_map)
    width = len(treasure_map[0])
    q = deque([src])
    visited = [[False] * width for _ in range(height)]
    visited[src[0]][src[1]] = True
    moves = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    length = 0
    while q:
        next_locs = deque()
        while q:
            next_locs.append(q.popleft())
        length += 1
        while next_locs:
            cr, cc = next_locs.popleft()
            for dr, dc in moves:
                nr, nc = cr + dr, cc + dc
                if 0 <= nr and nr < height and 0 <= nc and nc < width and not visited[nr][nc] and treasure_map[nr][nc]:
                    visited[nr][nc] = True
                    q.append((nr, nc))
    return length - 1



    
if __name__ == '__main__':  
    input = sys.stdin.readline
    height, width = map(int, input().split())
    treasure_map = [ None ] * height
    for i in range(height):
        treasure_map[i] = [0 if pos == 'W' else 1 for pos in input().rstrip()]
    curr_max = 0
    for r in range(height):
        for c in range(width):
            if treasure_map[r][c]:
                curr_max = max(curr_max, find_longest_path(treasure_map, (r, c)))
                
    print(curr_max)