from collections import defaultdict
class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        left_half = defaultdict(int)
        result = 0
        for n1 in nums1:
            for n2 in nums2:
                left_half[n1+n2] += 1
        for n3 in nums3:
            for n4 in nums4:
                result += left_half[-(n3 + n4)]
        return result
        
        
         