class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums_copy = nums[:]
        remove_duplicate = list(set(nums_copy))
        if len(nums_copy) == len(remove_duplicate):
            return False
        return True