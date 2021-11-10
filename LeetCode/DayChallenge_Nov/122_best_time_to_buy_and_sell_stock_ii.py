# time limit exceed! 
# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         n = len(prices)
#         DP = [0] * n
#         for i in range(1, n):
#             DP[i] = DP[i-1]
#             for j in range(i):
#                 DP[i] = max(DP[i], DP[j] + prices[i] - prices[j])
                
#         return DP[-1]
        
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        DP = [0] * n
        for i in range(1, n):
            DP[i] = DP[i-1]
            if prices[i] > prices[i-1]:
                DP[i] += prices[i] - prices[i-1]
                
        return DP[-1]
        