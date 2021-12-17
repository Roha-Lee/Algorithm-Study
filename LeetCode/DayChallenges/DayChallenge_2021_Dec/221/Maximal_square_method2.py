
arr = [3,1,3,2,2]
answer = 4 
stack = []
max_square = 0
for num in arr:
    width = 0 
    min_val = 100000000
    while stack and stack[-1] > num:
        val = stack.pop()
        width += 1
        min_val = min(val, min_val)
    max_square = min(width, min_val) ** 2
    stack.append(num)
print(max_square)

