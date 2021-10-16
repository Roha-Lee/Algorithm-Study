import sys
input = sys.stdin.readline
n = int(input())
nums = [int(input()) for _ in range(n)]

start = 1
stack = []
impossible = False
results = []
for num in nums:
    while num >= start:
        stack.append(start)
        start += 1
        results.append('+')    
    if num == stack.pop(): 
        results.append('-')
    else:
        impossible = True
        break

if impossible:
    print("NO")
else:
    print('\n'.join(results))