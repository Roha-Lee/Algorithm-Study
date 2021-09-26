class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1_dict = dict()
        nums2_dict = dict()

        for elem in nums1:
            nums1_dict.setdefault(elem, 0)
            nums1_dict[elem] += 1
        for elem in nums2:
            nums2_dict.setdefault(elem, 0)
            nums2_dict[elem] += 1

        intersection = set(nums1_dict.keys()).intersection(set(nums2_dict.keys()))
        result = []
        for key in intersection:
            result.extend([key] * min(nums1_dict[key], nums2_dict[key]))
        return result