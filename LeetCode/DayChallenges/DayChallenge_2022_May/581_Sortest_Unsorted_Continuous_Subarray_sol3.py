# Counting sort solution 
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        # Counting sort 
        MAX_NUM = 100000
        MIN_NUM = -100000
        counting = [0] * (MAX_NUM - MIN_NUM + 1)        
        sorted_nums = []
        for num in nums:
            counting[num + MIN_NUM] += 1
        for i in range(MIN_NUM, MAX_NUM + 1):
            while counting[i + MIN_NUM]:
                sorted_nums.append(i)
                counting[i + MIN_NUM] -= 1
        diff = [i for i in range(len(nums)) if nums[i] != sorted_nums[i]]
        if not diff:
            return 0 
        return max(diff) - min(diff) + 1    
        