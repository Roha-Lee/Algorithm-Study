class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1_core = nums1[:m]
        nums2_core = nums2[:]
        nums1_index = 0
        nums2_index = 0
        index = 0
        while nums1_index < m or nums2_index < n:
            nums1_elem = 1e9 + 1 if nums1_index == m else nums1_core[nums1_index]
            nums2_elem = 1e9 + 1 if nums2_index == n else nums2_core[nums2_index]
            if nums1_elem < nums2_elem:
                nums1[index] = nums1_elem
                nums1_index += 1
            else:
                nums1[index] = nums2_elem
                nums2_index += 1
            index += 1