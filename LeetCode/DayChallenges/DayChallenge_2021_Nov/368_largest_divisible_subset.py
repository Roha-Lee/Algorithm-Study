class Solution:       
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        DP = [0] * len(nums)
        prev = [-1] * len(nums)
        nums = sorted(nums)
        for i in range(len(nums)):
            DP[i] = 1
            for j in range(i):
                if nums[i] % nums[j] == 0 and DP[i] < DP[j] + 1:
                    DP[i] = DP[j] + 1
                    prev[i] = j
        result = []
        start = DP.index(max(DP))
        while start >= 0:
            result.append(nums[start])
            start = prev[start]
        return result