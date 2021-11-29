class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        DP = [0] * len(nums)
        DP[0] = nums[0]
        for i in range(1, len(nums)):
            DP[i] = max(nums[i], nums[i] + DP[i-1])
        return max(DP)