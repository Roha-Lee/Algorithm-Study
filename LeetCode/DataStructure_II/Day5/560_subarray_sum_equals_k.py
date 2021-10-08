class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        result = 0
        sum_value = 0
        hash_map = dict()
        for num in nums:    
            sum_value += num
            if sum_value - k == 0:
                result += 1
            if sum_value - k in hash_map.keys():
                result += hash_map[sum_value - k]
            hash_map.setdefault(sum_value, 0)
            hash_map[sum_value] += 1
            
        return result