# class Solution:
#     def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
#         DP = [0] * len(temperatures)
#         for i in range(len(DP)-2, -1, -1):
#             if temperatures[i] < temperatures[i+1]:
#                 DP[i] = 1
#             else:
#                 for j in range(i+1, len(DP)):
#                     if temperatures[i] < temperatures[j]:
#                         DP[i] = j - i
#                         break
#         return DP

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)
        stack = []
        for i in range(len(temperatures)):
            while stack and stack[-1][1] < temperatures[i]:
                idx, _ = stack.pop()
                answer[idx] = i - idx
            stack.append((i, temperatures[i]))
            

        return answer