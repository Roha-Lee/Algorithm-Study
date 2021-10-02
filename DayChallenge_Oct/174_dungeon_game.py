class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m = len(dungeon)
        n = len(dungeon[0])
        DP_mtx = [[-1e8 for _ in range(n+1)] for _ in range(m+1)]
        
        for j in range(n-1, -1, -1):
            for i in range(m-1, -1, -1):
                value = max(DP_mtx[i+1][j], DP_mtx[i][j+1])
                value = value if not value == -1e8 else 0 
                value += dungeon[i][j]
                value = 0 if value > 0 else value
                DP_mtx[i][j] = value
        if DP_mtx[0][0] >= 0:
            return 1
        else:
            return abs(DP_mtx[0][0]) + 1
            
        
        