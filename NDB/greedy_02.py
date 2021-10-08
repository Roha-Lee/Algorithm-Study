input_nums = list(map(int, list(input())))
result = input_nums[0]

for num in input_nums[1:]:
    if num <=1 or result <= 1:
        result += num
    else:
        result *= num

print(result)