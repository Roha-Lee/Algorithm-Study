class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)
        diff = [i for i in range(len(nums)) if nums[i] != sorted_nums[i]]
        if not diff:
            return 0 
        return max(diff) - min(diff) + 1