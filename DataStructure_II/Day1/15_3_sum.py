# Time Limit
# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         sorted_num = sorted(nums)
#         two_sum = [ [0]*len(nums) for _ in range(len(nums)) ]
#         for i in range(len(nums)):
#             for j in range(len(nums)):
#                 two_sum[i][j] = sorted_num[i] + sorted_num[j]
#                 if i == j:
#                     two_sum[i][j] = 2e5+1
#         results = set()
#         for start, num in enumerate(sorted_num):
#             for i in range(len(sorted_num)-1, start, -1):
#                 for j in range(len(sorted_num)-1, i-1, -1):
#                     if num + two_sum[j][i] == 0:
#                         results.add((num, sorted_num[i], sorted_num[j]))
        
#         return [[n1, n2, n3] for n1, n2, n3 in results]
            
        

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