import sys 
from operator import itemgetter
input = sys.stdin.readline
n = int(input())
coordinates = []
for _ in range(n):
    x, y = map(int, input().split())
    coordinates.append((x, y))
# coordinates = sorted(coordinates, key=itemgetter(0, 1))
coordinates = sorted(coordinates)
for x, y in coordinates:
    print(x, y)