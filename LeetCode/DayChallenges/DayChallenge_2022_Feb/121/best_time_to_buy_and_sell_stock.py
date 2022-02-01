class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        next_max = [0] * len(prices)
        next_max[-1] = prices[-1]
        for i in range(len(prices)-2, -1, -1):
            next_max[i] = prices[i] if prices[i] > next_max[i+1] else next_max[i+1]
            
        return max([sell - buy for sell, buy in zip(next_max, prices)])
            