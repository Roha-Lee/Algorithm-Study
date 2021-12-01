class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        len_nums = len(nums)
        offset = 0
        for idx in range(len_nums):
            num = nums[idx + offset]
            if num == 0:
                nums.pop(idx + offset)
                nums.insert(0, num)
            elif num == 2:
                nums.pop(idx + offset)
                nums.append(num)
                offset -= 1
            
            
        
        
            