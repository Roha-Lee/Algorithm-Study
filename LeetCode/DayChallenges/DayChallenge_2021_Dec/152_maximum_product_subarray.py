class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        result = -float('inf')
        
        prod = 1
        for num in nums:
            prod *= num
            result = max(prod, result)
            prod = 1 if prod == 0 else prod
        
        prod = 1
        for num in reversed(nums):
            prod *= num
            result = max(prod, result)
            prod = 1 if prod == 0 else prod
        
        return result