class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        left = 0
        right = len(nums) - 1
        while True:
            while left < len(nums) and not nums[left] % 2:
                left += 1
            while -1 < right and nums[right] % 2:
                right -= 1
            if not left < right:
                break
            nums[left], nums[right] = nums[right], nums[left]
        return nums