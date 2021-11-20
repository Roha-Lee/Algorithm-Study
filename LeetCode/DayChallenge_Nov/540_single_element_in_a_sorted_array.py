from bisect import bisect_left
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        start, end = 0, len(nums) - 1
        best = 0
        while start <= end:
            mid = (start + end) // 2
            loc = bisect_left(nums, nums[mid])
            if loc % 2 == 1:
                end = loc - 1
            else:
                best = mid
                start = loc + 2
        return nums[best]