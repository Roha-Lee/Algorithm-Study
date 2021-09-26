class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dic = dict()
        for num in nums:
            dic.setdefault(num, 0)
            dic[num] += 1
        for key, val in dic.items():
            if val == 1:
                return key
            

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        result = 0
        for num in nums:
            result ^= num
        return result
        