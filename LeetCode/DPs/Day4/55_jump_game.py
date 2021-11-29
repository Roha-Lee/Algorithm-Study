# TLE
# class Solution:
#     def canJump(self, nums: List[int]) -> bool:
#         DP = [False] * len(nums)
#         DP[0] = True
#         for idx, num in enumerate(nums):
#             if not DP[idx]:
#                 continue
#             for jump_length in range(1, num+1):
#                 if idx + jump_length < len(nums):
#                     DP[idx + jump_length] = True
#         return DP[-1]

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        DP = [False] * len(nums)
        DP[0] = True
        for idx, num in enumerate(nums):
            if not DP[idx]:
                continue
            if idx + num >= len(nums):
                return True
            for jump_length in range(1, num+1):
                DP[idx + jump_length] = True
                    
        return DP[-1]