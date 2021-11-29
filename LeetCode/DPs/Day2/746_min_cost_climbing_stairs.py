class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        DP = [0] * len(cost)
        DP[0], DP[1] = cost[0], cost[1]
        for i in range(2, len(cost)):
            DP[i] = cost[i] + min(DP[i-1], DP[i-2])
        return min(DP[-1], DP[-2])