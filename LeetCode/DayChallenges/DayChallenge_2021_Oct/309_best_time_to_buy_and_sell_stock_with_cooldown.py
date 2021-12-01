class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        DP = [0] * (len(prices) + 2)
        for i in range(len(prices)-2, -1, -1):
            DP[i] = DP[i+1]
            for j in range(i+1, len(prices)):
                DP[i] = max(DP[i], prices[j] - prices[i] + DP[j+2])
        return DP[0]