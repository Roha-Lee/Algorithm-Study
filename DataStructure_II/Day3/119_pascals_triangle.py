class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        cache = [1 for _ in range(rowIndex)]
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1, 1]
        for start in range(1, rowIndex):
            for idx in range(start, 0, -1):
                cache[idx] = cache[idx] + cache[idx-1]
        return cache + [1]
            