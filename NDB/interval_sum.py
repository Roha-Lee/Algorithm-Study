N = 10
nums = [100, 20, 1, 3, 5, 102, 42, 44, 73, 123]
M = [[1, 10], [2, 4], [3, 5], [5, 9], [8, 10]]
prefix_sum = [0] * (N+1)
prev = 0
for i in range(1, len(nums)+1):
    prefix_sum[i] = prev + nums[i-1]
    prev = prefix_sum[i]
print(prefix_sum)
for left, right in M:
    print(prefix_sum[right]-prefix_sum[left-1])
