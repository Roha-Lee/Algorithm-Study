class Solution:
    def _generate(self, permus, permu, nums):
        if len(permu) == len(nums):
            permus.append(permu[:])
            return 
        for num in nums:
            if num not in permu:
                permu.append(num)
                self._generate(permus, permu, nums)
                permu.pop()
    
    def permute(self, nums: List[int]) -> List[List[int]]:
        permus = []
        self._generate(permus, [], nums)
        return permus