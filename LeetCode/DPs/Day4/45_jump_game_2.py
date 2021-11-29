class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        DP = [0] * len(nums)
        curr_loc = 0
        while True:
            for i in range(1, nums[curr_loc]+1):
                if not DP[curr_loc + i]:
                    DP[curr_loc + i] = DP[curr_loc] + 1 
                if curr_loc + i == len(nums) - 1:
                    return DP[curr_loc + i]
            curr_loc += 1
            
        