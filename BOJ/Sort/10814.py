from operator import itemgetter
import sys

input = sys.stdin.readline
n = int(input())
members = []
for i in range(n):
    age, name = input().split()
    age = int(age)
    members.append((i, age, name))
members = sorted(members, key = itemgetter(1, 2))
for i, age, name in members:
    print(age, name)