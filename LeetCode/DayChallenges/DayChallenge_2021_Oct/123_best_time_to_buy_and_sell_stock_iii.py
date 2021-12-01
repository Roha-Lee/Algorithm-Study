class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        DP = [0] * len(prices)
        DP_rev = [0] * (len(prices)+1)
        
        min_val = prices[0]
        max_val = prices[0]
        for i in range(1, len(prices)):
            DP[i] = DP[i-1]
            if min_val > prices[i]:
                min_val = prices[i]
                max_val = prices[i]
            if max_val < prices[i]:
                max_val = prices[i]
                DP[i] = max_val - min_val
        
        min_val = prices[-1]
        max_val = prices[-1]
        for i in range(len(prices)-2, -1, -1):
            DP_rev[i] = DP_rev[i+1]
            if min_val > prices[i]:
                min_val = prices[i]
                DP_rev[i] = max_val - min_val
            if max_val < prices[i]:
                max_val = prices[i]
                min_val = prices[i]
        
        max_profit = 0
        for i in range(1, len(DP)+1):
            max_profit = max(max_profit, DP[i-1] + DP_rev[i])
        return max_profit