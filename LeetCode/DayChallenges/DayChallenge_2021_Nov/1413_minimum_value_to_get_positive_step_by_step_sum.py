class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        part_sum = 0
        min_sum = 0
        for i, num in enumerate(nums):
            part_sum += num
            min_sum = min(min_sum, part_sum)
        
        return 1 - min_sum
            