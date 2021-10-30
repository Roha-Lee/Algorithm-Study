class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0 
        right = len(nums) - 1
        best = 0 
        while left < right:
            mid = (left + right) // 2
            cen = nums[mid]
            lelem = nums[left]
            relem = nums[right]
            if cen > relem:
                left = mid + 1
            else:
                right = mid
                
            
        return nums[left]