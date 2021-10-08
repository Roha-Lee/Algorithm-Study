N = int(input())
fears = list(map(int, input().split()))

sorted_fears = sorted(fears)
result = 0

members = 0
for fear in sorted_fears:
    members += 1
    if fear <= members:
        result += 1
        members = 0
    
print(result)
