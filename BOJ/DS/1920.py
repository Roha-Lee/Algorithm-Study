import sys 
input = sys.stdin.readline
n = int(input())
nums = set(map(int, input().split()))
m = int(input())
queries = list(map(int, input().split()))
for query in queries:
    print(int(query in nums))