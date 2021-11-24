from collections import deque
class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        results = []
        first_idx = second_idx = 0 
        while first_idx < len(firstList) and second_idx < len(secondList):
            first, second = firstList[first_idx], secondList[second_idx]
            left = max(first[0], second[0])
            right = min(first[1], second[1])
            if left <= right:
                results.append([left, right])
            if first[1] < second[1]:
                first_idx += 1
            else:
                second_idx += 1
        return results