class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best_price = 1e4+1
        best_profit = 0
        for price in prices:
            if price - best_price > best_profit:
                best_profit = price - best_price
            if price < best_price:
                best_price = price
        return best_profit
        