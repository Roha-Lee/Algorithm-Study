class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)
        min_wrong, max_wrong = -1, -1
        for i in range(len(nums)):
            if nums[i] != sorted_nums[i]:
                min_wrong = i
                break
                
        for i in range(len(nums)-1, -1, -1):
            if nums[i] != sorted_nums[i]:
                max_wrong = i
                break
        if min_wrong == -1 or max_wrong == -1:
            return 0
        return max_wrong - min_wrong + 1