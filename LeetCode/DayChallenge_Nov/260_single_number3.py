class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor = 0 
        for i in range(len(nums)):
            xor ^= nums[i]
        mask = xor ^ (xor & (xor - 1))  
        result = 0
        for i in range(len(nums)):
            if nums[i] & mask:
                result ^= nums[i]
        return [result, xor ^ result]