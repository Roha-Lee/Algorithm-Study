class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)-1, -1, -1):
            if nums[i] == 0:
                nums.append(nums.pop(i))
            
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero = 0
        non_zero = 0
        n = len(nums)
        while True:
            while zero < n and nums[zero] != 0:
                zero += 1
            while non_zero < n and nums[non_zero] == 0:
                non_zero += 1
            if zero == n or non_zero == n:
                break
            if zero < non_zero:
                nums[zero], nums[non_zero] = nums[non_zero], nums[zero]
            else:
                non_zero += 1
            