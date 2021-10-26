
import math 
import sys 

def calc_walk(locations, left, right, m):
    walk = 0
    start = left 
    for book_left in range(left, 0, -1):
        gap = locations[start] - locations[start-1]
        k = math.ceil(book_left / m) - 1
        walk += gap * (2 * k + 1)
        start -= 1
    
    start = left + 1
    for book_left in range(right, 0, -1):
        gap = locations[start] - locations[start-1]
        k = math.ceil(book_left / m) - 1
        walk += gap * (2 * k + 1)
        start += 1
    
    walk += min(abs(locations[0]), abs(locations[-1]))

    return walk

input = sys.stdin.readline
n, m = map(int, input().split())
locations = sorted(list(map(int, input().split())) + [0])
left = locations.index(0)
right = n - locations.index(0)
walks = calc_walk(locations, left, right, m)
print(walks)