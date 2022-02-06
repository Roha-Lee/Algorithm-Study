import sys 
input = sys.stdin.readline
N = int(input())
print(sum([int(num) for num in list(input().strip())]))