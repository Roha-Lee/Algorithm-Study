class Solution:         
    def canPartition(self, nums: List[int]) -> bool:
        sum_nums = sum(nums)
        if(sum_nums % 2):
            return False
        target = sum_nums // 2
        
        DP = [0] * (target + 1)
        sorted_nums = sorted(nums, reverse=True)
        for num in sorted_nums:
            for curr_target in range(target, -1, -1):
                if curr_target >= num:
                    DP[curr_target] = max(DP[curr_target], DP[curr_target-num] + num)
                else:
                    break        
        
        return target == DP[-1]
        