class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        DP = [[0] * len(nums) for _ in range(2)]
        DP[0][0] = nums[0]
        DP[0][1] = nums[0]
        DP[1][1] = nums[1]
        for i in range(2, len(nums)):
            if i != len(nums) - 1: 
                DP[0][i] = max(DP[0][i-1], DP[0][i-2] + nums[i])
            DP[1][i] = max(DP[1][i-1], DP[1][i-2] + nums[i])
        return max(DP[0][-2], DP[1][-1])
        