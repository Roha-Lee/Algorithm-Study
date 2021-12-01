class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)
        prefix = 1
        for i in range(len(result)):
            result[i] *= prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(result)-1, -1, -1):
            result[i] *= postfix
            postfix *= nums[i]
            
        return result