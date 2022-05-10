from itertools import combinations
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = []
        for temp in combinations(range(1, 10), k):
            summation = sum(temp)
            if summation == n:
                result.append(list(temp))
        return result