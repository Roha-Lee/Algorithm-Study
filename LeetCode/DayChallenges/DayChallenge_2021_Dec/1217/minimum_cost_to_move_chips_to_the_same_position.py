class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        counts = [0, 0]
        for pos in position:
            counts[pos%2] += 1
        return min(counts)