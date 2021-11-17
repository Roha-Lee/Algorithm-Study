import sys 
def get_right_bigger_number(nums):
    result = [-1] * len(nums)
    stack = [(0, nums[0])]

    for i in range(1, len(nums)):
        while stack and nums[i] > stack[-1][1]:
            idx, _ = stack.pop()
            result[idx] = nums[i]
        stack.append((i, nums[i]))
    return result

    
if __name__ == '__main__':
    input = sys.stdin.readline
    n = int(input())
    nums = list(map(int, input().split()))
    print(*get_right_bigger_number(nums))