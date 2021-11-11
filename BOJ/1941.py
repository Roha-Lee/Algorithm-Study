import sys
def seven_princess(path, r, c, s, y=0):
    if y > 3:
        return 
    if len(path) == 7:
        possibles.add(tuple(sorted(path)))
        return 

    moves = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    adj = []
    for sr, sc in path: 
        for dr, dc in moves: 
            nr, nc = sr + dr, sc + dc 
            if 0 <= nr < 5 and 0 <= nc < 5 and (nr, nc) not in path:
                adj.append((nr, nc))
    for nr, nc in adj: 
        path.append((nr, nc))
        if seat_plan[nr][nc] == 'S':
            seven_princess(path, nr, nc, s + 1, y)
        else:
            seven_princess(path, nr, nc, s, y + 1)
        path.pop()
    
if __name__ == '__main__':
    input = sys.stdin.readline
    seat_plan = [input().rstrip() for _ in range(5)]
    possibles = set()
    for r in range(5):
        for c in range(5):
            if seat_plan[r][c] == 'S':
                seven_princess([(r, c)], r, c, s = 1)
    print(len(possibles))
    