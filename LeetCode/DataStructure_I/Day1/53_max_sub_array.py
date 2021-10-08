class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cumm_sum_list = [0] * len(nums)
        cumm_sum_list[0] = nums[0]
        for i in range(1, len(cumm_sum_list)):
            cumm_sum_list[i] = max(nums[i], nums[i] + cumm_sum_list[i-1])
        max_val = max(cumm_sum_list)
        return max_val
            
            