
arr = [0, 4, 3, 5, 0]
answer = 4 
stack = []
max_square = 0
width = 0
for num in arr:
    min_val = 100000000
    if num == 0:
        width = 0
    while stack and stack[-1] > num:
        val = stack.pop()
        width += 1
        min_val = min(val, min_val)
        # print(width, min_val)
        max_square = max(max_square, min(width, min_val) ** 2)
    stack.append(num)
print(max_square)

