class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums)<3: return False
        min_val = 2**31
        max_val = 2**31 
        for num in nums:
            if num <= min_val:
                min_val = num
            elif num <= max_val:
                max_val = num
            else:
                return True
        return False