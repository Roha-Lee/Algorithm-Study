class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0 
        end = len(nums) - 1
        while start <= end:
            mid = (start + end) // 2
            val = nums[mid]
            if val == target:
                return mid
            elif nums[start] <= val:
                if nums[start] <= target and target < val:
                    end = mid - 1
                else:
                    start = mid + 1
            else:
                if val < target and target <= nums[end]:
                    start = mid + 1
                else:
                    end = mid - 1
        return -1