class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_num = sorted(nums)
        added = set()
        results = list()
        for index, num in enumerate(sorted_num):
            start = index + 1
            end = len(sorted_num) - 1
            while start < end:
                num1 = sorted_num[start]
                num2 = sorted_num[end]
                if num + num1 + num2 == 0:
                    if (num, num1, num2) not in added:
                        added.add((num, num1, num2))
                        results.append([num, num1, num2])
                    else:
                        start += 1
                elif num + num1 + num2 > 0:
                    end -= 1
                else:
                    start += 1
        return results