N = int(input())
plans = input().split() 

MOVE_DICT = {
    'R': (0, 1),
    'L': (0, -1),
    'U': (-1, 0),
    'D': (1, 0)
}

x, y = (1, 1)
for plan in plans:
    dx, dy = MOVE_DICT[plan]
    x = x + dx if x + dx >= 1 and x + dx <= N else x
    y = y + dy if y + dy >= 1 and y + dy <= N else y

print(x, y)
