import sys 
input = sys.stdin.readline
n = int(input())
heights = [int(input()) for _ in range(n)]

left = right = 0
l_prev_max = r_prev_max = 0
for i in range(len(heights)):
    if l_prev_max < heights[i]:
        left += 1
        l_prev_max = heights[i]
    if r_prev_max < heights[-i-1]:
        right += 1
        r_prev_max = heights[-i-1]
print(left)
print(right)
    
