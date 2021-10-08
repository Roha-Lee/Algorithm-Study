class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cnt = 0
        major = nums[0]
        for num in nums:
            if major == num:
                cnt += 1
            else:
                cnt -= 1
            if cnt < 0:
                major = num
                cnt = 0
        return major