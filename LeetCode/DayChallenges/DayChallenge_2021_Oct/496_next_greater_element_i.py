from collections import defaultdict
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        _nums1 = {v:i for i, v in enumerate(nums1)}
        results = [-1] * len(nums1)
        for num in nums2:
            while stack and stack[-1] < num:
                results[_nums1[stack.pop()]] = num
            if num in _nums1:
                stack.append(num)
        return results    
        