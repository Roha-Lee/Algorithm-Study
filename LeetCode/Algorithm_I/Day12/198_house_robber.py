class Solution:
    def rob(self, nums: List[int]) -> int:
        DP = [0] * len(nums)
        for i in range(len(nums)):
            if i >= 2:
                DP[i] = max(DP[i-2] + nums[i], DP[i-1])
            elif i >= 1:
                DP[i] = max(DP[i-1], nums[i])
            else:
                DP[i] = nums[i]
        return DP[-1]