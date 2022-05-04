from collections import Counter 
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        counter = Counter(nums)
        operation = 0
        for key in counter:
            operation += min(counter[key], counter[k - key])
        return operation // 2
            