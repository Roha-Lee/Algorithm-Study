class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left, right = 0, len(nums)-1
        while left <= right: 
            mid = (left + right) // 2
            cen = nums[mid]
            bef = nums[mid-1] if mid-1 >= 0 else -float('inf')
            aft = nums[mid+1] if mid+1 < len(nums) else -float('inf')
            if bef < cen and cen > aft: 
                return mid
            elif bef < cen and cen < aft:
                left = mid + 1
            elif bef > cen and cen < aft:
                left = mid + 1
            else:
                right = mid - 1
            