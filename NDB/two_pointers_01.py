nums = [1,2,3,2,5]
M = 4
start = 0
end = 0
cnt = 0
curr = nums[start]
while start < len(nums) or end < len(nums):
    if curr < M:
        if end < len(nums)-1:
            end += 1
            curr += nums[end]
        else:
            break
    elif curr >= M:
        if curr == M:
            cnt += 1
    
        if start < len(nums)-1:
            curr -= nums[start]
            start += 1
        else:
            break
print(cnt)