from collections import Counter
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        cntr = Counter(nums)
        max_num = max(nums)
        DP = [0] * (max_num + 1)
        DP[1] = cntr[1]
        for i in range(2, max_num+1):
            DP[i] = max(DP[i-2] + i * cntr[i], DP[i-1])
        return DP[-1]
        